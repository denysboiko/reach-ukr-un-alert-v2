import os
import psycopg2
from django.utils.translation import ugettext_lazy as _


import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ['DEBUG']
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com'
]

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.core.mail',
    'widget_tweaks',
    'rest_framework',
    'guardian',
    'colorfield',
    'AlertsMap.apps.AlertSystemConfig',
    'modeltranslation'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 250
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'alerts_map.urls'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # default
    'guardian.backends.ObjectPermissionBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'alerts_map.wsgi.application'

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'alert_system',
            'USER': 'denysboiko',
            'PASSWORD': 'csdjhjnrf4',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'ebdb',
    #         'USER': 'dbadmin',
    #         'PASSWORD': 'pgk6vsnA',
    #         'HOST': 'aa1jnxr5cnvhbxx.cjzycczlrnst.eu-west-1.rds.amazonaws.com',
    #         # aa1jnxr5cnvhbxx.cjzycczlrnst.eu-west-1.rds.amazonaws.com:5432
    #         'PORT': '5432',
    #     }
    # }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

LANGUAGES = (

    ('en', _('English')),
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),

)

# ru-RU
# en-us
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Authorization

AUTH_USER_MODEL = 'AlertsMap.User'

# Email settings

DEFAULT_FROM_EMAIL = 'denys.boiko@reach-initiative.org'
MODERATION_MODERATORS = ['denys.boiko@reach-initiative.org']

# SECURITY WARNING: use environment variables in production!
EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'AKIAIR7B2ZEUPYAM7EFA'
EMAIL_HOST_PASSWORD = 'ApNOSctoPCro+lC//G/tEZPGK6S4IDBBnBlTKwh/4zMs'
EMAIL_USE_TLS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

SITE_ID = 1
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'AlertsMap', 'static')
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
