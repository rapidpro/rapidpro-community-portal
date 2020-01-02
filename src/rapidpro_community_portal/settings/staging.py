from rapidpro_community_portal.settings.base import *  # noqa

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')  # noqa
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')  # noqa

DEBUG = os.environ.get('DEBUG', False)  # noqa

DATABASES['default']['NAME'] = os.environ.get('DB_NAME', 'rapidpro_community_portal_staging')  # noqa
DATABASES['default']['USER'] = os.environ.get('DB_USER', 'rapidpro_community_portal_staging')  # noqa
DATABASES['default']['HOST'] = os.environ.get('DB_HOST', '')  # noqa
DATABASES['default']['PORT'] = os.environ.get('DB_PORT', '')  # noqa
DATABASES['default']['PASSWORD'] = os.environ.get('DB_PASSWORD', '')  # noqa

WEBSERVER_ROOT = '/var/www/rapidpro_community_portal/'
PUBLIC_ROOT = os.path.join(WEBSERVER_ROOT, 'public')  # noqa
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')  # noqa
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')  # noqa
# LOGGING['handlers']['file']['filename'] = os.path.join(WEBSERVER_ROOT, 'log', 'rapidpro_community_portal.log')  # noqa

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '%(CACHE_HOST)s' % os.environ,  # noqa
    }
}

EMAIL_SUBJECT_PREFIX = '[Rapidpro_Community_Portal Staging] '

COMPRESS_ENABLED = True

SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', True)  # noqa
SESSION_COOKIE_HTTPONLY = os.environ.get('SESSION_COOKIE_HTTPONLY', True)  # noqa
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', True)  # noqa
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', True)  # noqa


ALLOWED_HOSTS = (
    'localhost',
    '0.0.0.0',
    '127.0.0.1'
)

# ALLOWED_HOSTS = [
#     os.environ.get('ALLOWED_HOSTS', 'localhost').split(';')
# ] + ['0.0.0.0']

# Used by Wagtail in sending emails for moderation
BASE_URL = 'https://rapidpro-staging.cakt.us'

# Uncomment if using celery worker configuration
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'amqp://rapidpro_community_portal_staging:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/rapidpro_community_portal_staging' % os.environ  # noqa
