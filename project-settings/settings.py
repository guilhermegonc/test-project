import os
import django_heroku
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Key and Hosts
DEBUG = config('DEBUG') == 'True'
ALLOWED_HOSTS = ['http://guilhermegoncalves.herokuapp.com']
SECRET_KEY = config('SECRET_KEY')

DB_NAME = config('DB_NAME')
DB_HOST = config('DB_HOST')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "auth0",
    "app",
    "forms",
    "tic_tac_toe",
    "smart_home",
    "menu"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project-settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "project-settings.wsgi.application"


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Authentication
SOCIAL_ATUH_TRAILING_SLASH = False
SOCIAL_AUTH_AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
SOCIAL_AUTH_AUTH0_KEY = os.environ.get('AUTH0_CLIENT_ID')
SOCIAL_AUTH_AUTH0_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email',
    'name'
]

AUTHENTICATION_BACKENDS = {
    'auth0.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend'
}

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/dashboard'


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

django_heroku.settings(locals())
