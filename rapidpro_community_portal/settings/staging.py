from rapidpro_community_portal.settings.base import *  # noqa

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['NAME'] = 'rapidpro_community_portal_staging'
DATABASES['default']['USER'] = 'rapidpro_community_portal_staging'
DATABASES['default']['HOST'] = os.environ.get('DB_HOST', '')
DATABASES['default']['PORT'] = os.environ.get('DB_PORT', '')
DATABASES['default']['PASSWORD'] = os.environ['DB_PASSWORD']

WEBSERVER_ROOT = '/var/www/rapidpro_community_portal/'

PUBLIC_ROOT = os.path.join(WEBSERVER_ROOT, 'public')

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

LOGGING['handlers']['file']['filename'] = os.path.join(
    WEBSERVER_ROOT, 'log', 'rapidpro_community_portal.log')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '%(CACHE_HOST)s' % os.environ,
    }
}

EMAIL_SUBJECT_PREFIX = '[Rapidpro_Community_Portal Staging] '

COMPRESS_ENABLED = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(';')

# Used by Wagtail in sending emails for moderation
BASE_URL = 'https://rapidpro-staging.cakt.us'

# Uncomment if using celery worker configuration
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'amqp://rapidpro_community_portal_staging:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/rapidpro_community_portal_staging' % os.environ  # noqa
