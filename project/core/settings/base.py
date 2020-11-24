from decouple import config
from pathlib import Path


# Main
BASE_DIR = Path(__file__).resolve().parent.parent.parent # path example: BASE_DIR / 'subdir'
SECRET_KEY = config('SECRET_KEY')

# Etc
WSGI_APPLICATION = 'core.wsgi.application'
FIXTURE_DIRS = ('/fixtures/',)
ROOT_URLCONF = 'core.urls'


# Auth
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'accounts:login_done'
LOGOUT_REDIRECT_URL = 'accounts:logout_done'


# Apps
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Static files
STATIC_URL = '/static/' # URL prefix for static files
STATIC_ROOT = BASE_DIR / 'static' # Where static files should be collected
STATICFILES_DIRS = [ BASE_DIR / 'ui/assets' ] # Additional locations


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
