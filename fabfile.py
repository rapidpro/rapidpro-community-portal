import os
import tempfile
import time

import yaml

from fabric.api import env, execute, get, hide, cd, lcd, local, put, require, run, settings, sudo, task
from fabric.colors import red
from fabric.contrib import files, project, console
from fabric.contrib.console import confirm
from fabric.utils import abort

DEFAULT_SALT_LOGLEVEL = 'info'
PROJECT_ROOT = os.path.dirname(__file__)
CONF_ROOT = os.path.join(PROJECT_ROOT, 'conf')

VALID_ROLES = (
    'salt-master',
    'web',
    'worker',
    'balancer',
    'db-master',
    'queue',
    'cache',
)


envs = {
    'staging': {
        'master': '107.20.144.189',
        'host_string': 'rapidpro-staging.cakt.us',

    },
    'production': {
        'master': '54.77.58.154',
        'host_string': 'rapidpro-prod.cakt.us',
    },
    'local': {
        'user': 'vagrant',
    }
}


def _common_env():
    env.forward_agent = True
    env.project = 'rapidpro_community_portal'
    env.project_root = os.path.join('/var', 'www', env.project)
    for key, value in envs[env.environment].items():
        setattr(env, key, value)


@task
def staging():
    env.environment = 'staging'
    _common_env()


@task
def production():
    env.environment = 'production'
    _common_env()


@task
def vagrant():
    env.environment = 'local'
    _common_env()
    # convert vagrant's ssh-config output to a dictionary
    ssh_config_output = local('vagrant ssh-config', capture=True)
    ssh_config = dict(line.split() for line in ssh_config_output.splitlines())
    env.master = '{HostName}:{Port}'.format(**ssh_config)
    env.key_filename = ssh_config['IdentityFile']


@task
def setup_master():
    """Provision master with salt-master."""
    with settings(warn_only=True):
        with hide('running', 'stdout', 'stderr'):
            installed = run('which salt')
    if not installed:
        sudo('apt-get update -qq -y')
        sudo('apt-get install python-software-properties -qq -y')
        sudo('add-apt-repository ppa:saltstack/salt -y')
        sudo('apt-get update -qq')
        sudo('apt-get install salt-master -qq -y')
    # make sure git is installed for gitfs
    with settings(warn_only=True):
        with hide('running', 'stdout', 'stderr'):
            installed = run('which git')
    if not installed:
        sudo('apt-get install python-pip git-core python-git -qq -y')
    put(local_path='conf/master.conf', remote_path="/etc/salt/master", use_sudo=True)
    sudo('service salt-master restart')


@task
def sync():
    """Rysnc local states and pillar data to the master."""
    # Check for missing local secrets so that they don't get deleted
    # project.rsync_project fails if host is not set
    with settings(host=env.master, host_string=env.master):
        if not have_secrets():
            get_secrets()
        else:
            # Check for differences in the secrets files
            for environment in ['staging', 'production']:
                remote_file = os.path.join('/srv/pillar/', environment, 'secrets.sls')
                with lcd(os.path.join(CONF_ROOT, 'pillar', environment)):
                    if files.exists(remote_file):
                        get(remote_file, 'secrets.sls.remote')
                    else:
                        local('touch secrets.sls.remote')
                    with settings(warn_only=True):
                        result = local('diff -u secrets.sls.remote secrets.sls')
                        if (result.failed and
                            not confirm(red(
                                "Above changes will be made to secrets.sls. Continue?"))):
                            abort(
                                "Aborted. File have been copied to secrets.sls.remote. " +
                                "Resolve conflicts, then retry.")
                        else:
                            local("rm secrets.sls.remote")
        salt_root = CONF_ROOT if CONF_ROOT.endswith('/') else CONF_ROOT + '/'
        project.rsync_project(local_dir=salt_root, remote_dir='/tmp/salt', delete=True)
        sudo('rm -rf /srv/salt /srv/pillar')
        sudo('mv /tmp/salt/* /srv/')
        sudo('rm -rf /tmp/salt/')


def have_secrets():
    """Check if the local secret files exist for all environments."""
    found = True
    for environment in ['staging', 'production']:
        local_file = os.path.join(CONF_ROOT, 'pillar', environment, 'secrets.sls')
        found = found and os.path.exists(local_file)
    return found


@task
def get_secrets():
    """Grab the latest secrets file from the master."""
    with settings(host=env.master):
        for environment in ['staging', 'production']:
            local_file = os.path.join(CONF_ROOT, 'pillar', environment, 'secrets.sls')
            if os.path.exists(local_file):
                local('cp {0} {0}.bak'.format(local_file))
            remote_file = os.path.join('/srv/pillar/', environment, 'secrets.sls')
            get(remote_file, local_file)


@task
def setup_minion(*roles):
    """Setup a minion server with a set of roles."""
    require('environment')
    for r in roles:
        if r not in VALID_ROLES:
            abort('%s is not a valid server role for this project.' % r)
    # install salt minion if it's not there already
    with settings(warn_only=True):
        with hide('running', 'stdout', 'stderr'):
            installed = run('which salt-minion')
    if not installed:
        # install salt-minion from PPA
        sudo('apt-get update -qq -y')
        sudo('apt-get install python-software-properties -qq -y')
        sudo('add-apt-repository ppa:saltstack/salt -y')
        sudo('apt-get update -qq')
        sudo('apt-get install salt-minion -qq -y')
    config = {
        'master': 'localhost' if env.master == env.host else env.master,
        'output': 'mixed',
        'grains': {
            'environment': env.environment,
            'roles': list(roles),
        },
        'mine_functions': {
            'network.interfaces': []
        },
    }
    _, path = tempfile.mkstemp()
    with open(path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    put(local_path=path, remote_path="/etc/salt/minion", use_sudo=True)
    sudo('service salt-minion restart')
    # queries server for its fully qualified domain name to get minion id
    key_name = run('python -c "import socket; print socket.getfqdn()"')
    time.sleep(5)
    execute(accept_key, key_name)


@task
def add_role(name):
    """Add a role to an exising minion configuration."""
    if name not in VALID_ROLES:
        abort('%s is not a valid server role for this project.' % name)
    _, path = tempfile.mkstemp()
    get("/etc/salt/minion", path)
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    grains = config.get('grains', {})
    roles = grains.get('roles', [])
    if name not in roles:
        roles.append(name)
    else:
        abort('Server is already configured with the %s role.' % name)
    grains['roles'] = roles
    config['grains'] = grains
    with open(path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    put(local_path=path, remote_path="/etc/salt/minion", use_sudo=True)
    sudo('service salt-minion restart')


@task
def salt(cmd, target="'*'", loglevel=DEFAULT_SALT_LOGLEVEL):
    """Run arbitrary salt commands."""
    with settings(warn_only=True, host_string=env.master):
        sudo("salt -v {0} -l{1} {2} ".format(target, loglevel, cmd))


@task
def highstate(target="'*'", loglevel=DEFAULT_SALT_LOGLEVEL):
    """Run highstate on master."""
    with settings(host_string=env.master):
        print("This can take a long time without output, be patient")
        salt('state.highstate', target, loglevel)


@task
def accept_key(name):
    """Accept minion key on master."""
    with settings(host_string=env.master):
        sudo('salt-key --accept={0} -y'.format(name))
        sudo('salt-key -L')


@task
def delete_key(name):
    """Delete specific key on master."""
    with settings(host_string=env.master):
        sudo('salt-key -L')
        sudo('salt-key --delete={0} -y'.format(name))
        sudo('salt-key -L')


@task
def deploy(loglevel=DEFAULT_SALT_LOGLEVEL):
    """Deploy to a given environment by pushing the latest states and executing the highstate."""
    require('environment')
    with settings(host_string=env.master):
        if env.environment != "local":
            sync()
        target = "-G 'environment:{0}'".format(env.environment)
        salt('saltutil.sync_all', target, loglevel)
        highstate(target)


@task
def manage_run(command):
    """
    Run a Django management command on the remote server.
    """
    require('environment')
    # Setup the call
    manage_sh = u"/var/www/{project}/manage.sh ".format(**env)
    sudo(manage_sh + command, user=env.project)


@task
def manage_shell():
    manage_run('shell')


@task
def get_db_dump(clean=False):
    """Get db dump of remote enviroment."""
    require('environment')
    db_name = '%(project)s_%(environment)s' % env
    dump_file = db_name + '.sql' % env
    project_root = os.path.join('/var', 'www', env.project)
    temp_file = os.path.join(project_root, dump_file)
    flags = '-Ox'
    if clean:
        flags += 'c'
    dump_command = 'pg_dump %s %s -U %s > %s' % (flags, db_name, db_name, temp_file)
    with settings(host_string=env.host_string):
        sudo(dump_command, user=env.project)
        get(temp_file, dump_file)


@task
def reset_local_db():
    """ Reset local database from remote host """
    require('environment')
    question = 'Are you sure you want to reset your local ' \
               'database with the %(environment)s database?' % env
    if not console.confirm(question, default=False):
        abort('Local database reset aborted.')
    remote_db_name = '%(project)s_%(environment)s' % env
    db_dump_name = remote_db_name + '.sql'
    local_db_name = env.project
    get_db_dump()
    with settings(warn_only=True):
        local('dropdb %s' % local_db_name)
    local('createdb -E UTF-8 %s' % local_db_name)
    local('cat %s | psql %s' % (db_dump_name, local_db_name))


@task
def reset_local_media():
    """ Reset local media from remote host """
    require('environment')
    media_source = os.path.join('/var', 'www', env.project, 'public', 'media')
    media_target = os.path.join(PROJECT_ROOT, 'public')
    with settings():
        local("rsync -rvaz %s:%s %s" % (env.master, media_source, media_target))


@task
def refresh_environment():
    require('environment')
    if env.environment == 'production':
        abort('Production cannot be refreshed!')

    source_env = 'production'

    db_name = '%s_%s' % (env.project, source_env)
    dump_file_name = '%s.sql' % db_name
    full_dump_file_path = os.path.join(env.project_root, dump_file_name)
    src_env_host = envs[source_env]['host_string']

    with settings(host_string=src_env_host):
        sudo('pg_dump -Ox %s -U %s > %s' % (db_name, db_name, full_dump_file_path))

    sudo('supervisorctl stop all')
    db_name = db_user = '%s_%s' % (env.project, env.environment)
    media_full_path = '%s/public/media' % env.project_root
    with cd('/tmp'):
        run('scp %s:%s %s' % (src_env_host, full_dump_file_path, dump_file_name))
        sudo('dropdb %s_backup' % db_name, user='postgres')
        sudo('psql -c "alter database %s rename to %s_backup"' % (db_name, db_name), user='postgres')
        sudo('createdb -E UTF-8 -O %s %s' % (db_user, db_name), user='postgres')
        sudo('psql -U %s -d %s -f %s' % (db_user, db_name, dump_file_name))
        run('rsync -zPae ssh %s:%s .' % (src_env_host, media_full_path))
        sudo('rm -rf %s.backup' % media_full_path)
        sudo('mv %s %s.backup' % (media_full_path, media_full_path))
        sudo('mv media %s' % media_full_path)
        sudo('chown -R %s:%s %s' % (env.project, env.project, media_full_path))

    manage_run("migrate")
    sudo('supervisorctl start all')
