"""
Django settings for shoaibCommerece project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-as%-l6tn-u8pwckha*bw2rgjp%-dq=6ik*xnks7g0u%sg6ti4x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ssl-ql97.onrender.com']

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login_old/'
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

STRIPE_API_KEY_PUBLISHABLE = 'pk_test_51NaWhJJQmh7tshf7UBjp671cyquBm44eQwmq9viZu0MEWyxK3f0HDLrTi6RT3LS5E5vjF8kPgNCzmtzmdY2cSFLn00MVfxIY9r'
STRIPE_API_KEY_HIDDEN = 'sk_test_51NaWhJJQmh7tshf7PIGDbhCSEKypRH8l8P3mxMKcMde3zGtlQZEXyY8M1D74Unj7JyfmuBXfUPqMliSNvaBUJN1e00f2a8011D'
#Live keys:
#STRIPE_API_KEY_PUBLISHABLE = 'pk_live_51NaWhJJQmh7tshf7pNLqsbalVU4UYfOF4SHCggmlUmFtIhFREEHxSJGQIg6CVBMwezAIRExQWiVf12e5nXIaZjci00mmJZrK1Z'
#STRIPE_API_KEY_HIDDEN = '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'


# Application definition

INSTALLED_APPS = [
    'CommerceApp',
    'crispy_forms',
    'crispy_bootstrap5',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shoaibCommerece.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'CommerceApp.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'shoaibCommerece.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
import os
STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
#SMTP Confg:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shoaib4311859@gmail.com'
EMAIL_HOST_PASSWORD = 'wofegltuqmpfafkl'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

