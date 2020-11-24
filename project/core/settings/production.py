from .base import *
from decouple import config


# Main
DEBUG = False

# Etc
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1', 'localhost']

# Debug toolbar
def showToolbar():
    return DEBUG

SHOW_TOOLBAR_CALLBACK = showToolbar

# Email
DEFAULT_FROM_EMAIL = 'figline@localhost'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Apps
INSTALLED_APPS = BASE_APPS + [
    'django_filters',
    'debug_toolbar',
    'apps.accounts',
    'apps.landing',
    'apps.tools',
    'apps.ingredients',
    'apps.recipes'
]


# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_DATABASE'),
        'USER': config('MYSQL_USER'),
        'PASSWORD': config('MYSQL_PASSWORD'),
        'HOST': config('MYSQL_HOST'),
        'PORT': config('MYSQL_PORT'),
        'TEST': {
            'NAME': config('MYSQL_DATABASE_TEST'),
        },
    }
}


# Password validation
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




