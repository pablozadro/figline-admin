from .base import *
from decouple import config


# Main
DEBUG = True

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
    'rest_framework',
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}