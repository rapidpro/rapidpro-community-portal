# Django settings for rapidpro_community_portal project.
import os
from pathlib import Path

import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

env = environ.Env()
environ.Env.read_env()

PROJECT_ROOT = env.str('PROJECT_ROOT', os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
DEBUG = env.bool('DEBUG', False)

ADMINS = (
    ('RapidPro Dev Team', 'rapidpro-team@caktusgroup.com'),
)

DATABASES = {'default': env.db()}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


AZURE_ACCOUNT_NAME = env.str('AZURE_ACCOUNT_NAME', 'sauniwebsaksio')
AZURE_ACCOUNT_KEY = env.str('AZURE_ACCOUNT_KEY', None)
AZURE_CONTAINER = env.str('AZURE_CONTAINER', 'rapidpro-community')

if AZURE_ACCOUNT_KEY:
    AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
    AZURE_SSL = True
    AZURE_AUTO_SIGN = True
    MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'rapidpro_community_portal.config.storages.AzureMediaStorage'
    AZURE_CONNECTION_TIMEOUT_SECS = 120
    AZURE_URL_EXPIRATION_SECS = 7200

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zy)@smb_q+s&hc97uv#)*-+arl#l0yy&3(7k937f6v7+k_6ckz'
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True


MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'rapidpro_community_portal.config.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'rapidpro_community_portal.config.wsgi.application'

SETTINGS_DIR = Path(__file__).parent
PACKAGE_DIR = SETTINGS_DIR.parent
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PACKAGE_DIR / 'templates')
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
                'i18n': 'django.templatetags.i18n',
            },
        },
    },
]

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # External apps
    'storages',
    'compressor',
    'corsheaders',
    'taggit',
    'modelcluster',
    'django.contrib.admin',
    'wagtail.core',
    'wagtail.admin',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail.images',
    'wagtail.embeds',
    'wagtail.search',
    'wagtail.contrib.redirects',
    'wagtail.contrib.forms',
    'wagtail.sites',
    'wagtail.contrib.routable_page',
    # project apps
    'rapidpro_community_portal.apps.accounts',
    'rapidpro_community_portal.apps.portal_pages',
    'rapidpro_community_portal',
)

AUTH_USER_MODEL = 'accounts.RapidProUser'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(BASE_DIR, 'rapidpro_community_portal.log'),
            'maxBytes': 10 * 1024 * 1024,  # 10 MB
            'backupCount': 10,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rapidpro_community_portal': {
            'handlers': ['file', 'mail_admins'],
            'level': 'INFO',
        },
    }
}

ALLOWED_HOSTS = env.str('ALLOWED_HOSTS', 'localhost').split(';') + ['0.0.0.0']

CACHE_HOST = env.bool('CACHE_HOST', '127.0.0.1:11211')
BROKER_HOST = env.bool('BROKER_HOST', '127.0.0.1:5672')
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': CACHE_HOST
    }
}

SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', True)
SESSION_COOKIE_HTTPONLY = env.bool('SESSION_COOKIE_HTTPONLY', True)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', True)
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', True)


# Application settings
COMPRESS_ENABLED = env.bool('COMPRESS_ENABLED', True)
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

WAGTAIL_SITE_NAME = 'RapidPro'
LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

# Used by Wagtail in sending emails for moderation
BASE_URL = 'http://localhost:8000'

DEFAULT_FROM_EMAIL = 'noreply@community.rapidpro.io'
EMAIL_SUBJECT_PREFIX = env.str('EMAIL_SUBJECT_PREFIX', '[Rapidpro_Community_Portal] ')

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.HalloRichTextArea'
    }
}

CELERY_TASK_ALWAYS_EAGER = env.bool('CELERY_TASK_ALWAYS_EAGER', False)
CELERY_EAGER_PROPAGATES_EXCEPTIONS = env.bool('CELERY_EAGER_PROPAGATES_EXCEPTIONS', False)

SENTRY_DSN = env.str('SENTRY_DSN', None)  # noqa: F405
if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, send_default_pii=True, integrations=[DjangoIntegration(), ])

if DEBUG:  # pragma: no cover

    INSTALLED_APPS += ('debug_toolbar', )
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    DEBUG_TOOLBAR_CONFIG = {'SHOW_TEMPLATE_CONTEXT': True}
