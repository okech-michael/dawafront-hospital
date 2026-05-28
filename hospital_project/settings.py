from pathlib import Path
import os
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-dawafront-healthcare-secret-key-change-in-production')

DEBUG = config('DEBUG', default=True, cast=bool)

# Allow Vercel domains, Railway, Netlify, and localhost
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',
    '.railway.app',
    '.netlify.app',
    'dawafront-hospital.vercel.app',
    'dawafront-hospital.netlify.app',
]

# Override with environment variable if provided
_allowed_hosts_env = config('ALLOWED_HOSTS', default=None)
if _allowed_hosts_env:
    ALLOWED_HOSTS = _allowed_hosts_env.split(',')

CSRF_TRUSTED_ORIGINS = [
    'https://dawafront-hospital.up.railway.app',
    'https://*.railway.app',
    'https://*.vercel.app',
    'https://dawafront-hospital.vercel.app',
    'https://*.netlify.app',
    'https://dawafront-hospital.netlify.app',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospital_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hospital_project.wsgi.application'

# Database configuration
try:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default='sqlite:///db.sqlite3',
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
except Exception as e:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'main_app' / 'static',
]

# Use simple static files storage - no hashing or compression
# This works better on serverless platforms like Vercel
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Static root - when DEBUG=False on production, Django needs STATIC_ROOT
# When DEBUG=True (Vercel), files served from STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Disable WhiteNoise compression to avoid issues
WHITENOISE_AUTOREFRESH = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
