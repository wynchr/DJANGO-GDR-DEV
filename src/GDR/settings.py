"""
=======================================================================================================================
.DESCRIPTION
    Django settings for GDR project.

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    TO DEBUG CSS QUICKLY
    python manage.py livereload
=======================================================================================================================
"""
from pathlib import Path
import os
import platform
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# import ENVIRONMENT settings
env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR / "GDR" / ".env"))

# GLOBAL INFO
INFO_APPS = {
    'application': 'RefId',
    'version': '1.1.86',
    'environment': env("ENV"),
    'machine': platform.uname().node,
    'user': os.getlogin(),
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['10.20.180.155', 'BD22089', '.localhost', '127.0.0.1', '[::1]']

APPEND_SLASH = True

WSGI_APPLICATION = 'GDR.wsgi.application'

ROOT_URLCONF = 'GDR.urls'

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livereload',
    'django_cleanup',
    'crispy_forms',
    'crispy_bootstrap5',
    'multiselectfield',
    'refid',
    'tests',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
]

# python manage.py livereload

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
            BASE_DIR / "GDR" / "templates",
        ],
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

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env("DB_ENGINE"),
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    },
}

# pprint.pprint(DATABASES)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# DATE_INPUT_FORMATS = '%d-%m-%Y'
# SHORT_DATE_FORMAT = '%d-%m-%Y'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static"  # python manage.py collectstatic

STATICFILES_DIRS = [
    BASE_DIR / "GDR" / "static",
]

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'GDR' / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# LOGIN_REDIRECT_URL = 'dashboard'
#
# LOGOUT_REDIRECT_URL = 'home'
#
# LOGIN_URL = 'login'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'


