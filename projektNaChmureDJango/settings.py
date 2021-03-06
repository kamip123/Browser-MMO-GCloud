"""
Django settings for projektNaChmureDJango project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%hvda=l7_z0&lw%gljyv6_5m59p7y3#bqb!jz=@k%df_704w8_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cityMap',
    'mainPage',
    'rankings',
    'worldMap',
    'messagess',
    'alliance',
    'raports',
    'premium',
    'profileUser',
    'kontakt',
    'rest_framework',
    'background_task',
    'scheduleTasks',
    'paypal.standard.ipn',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'projektNaChmureDJango.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'projektNaChmureDJango.wsgi.application'


AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#MEDIA_ROOT = 'https://console.cloud.google.com/storage/solwit-pjatk-arc-2018-gr1.appspot.com'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# LOGIN_REDIRECT_URL = '/mainPage/templates/index.html'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
     ),
}


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kontonazajecia123@gmail.com'
EMAIL_HOST_PASSWORD = 'zsadsadaA1'
EMAIL_PORT = 587


PAYPAL_RECEIVER_EMAIL = 'parzyjaglakamil@gmail.com'
#PAYPAL_IDENTITY_TOKEN = 'KrMpKsJG09azuxURUTJhvXG2HKgGSJV_DNYeVYxhdIlrgSlTwOFpUXlo2re'
PAYPAL_TEST = True

EMAIL_HOST_USER = 'kontonazajecia123@gmail.com'
EMAIL_HOST_PASSWORD = 'zsadsadaA1'

SOCIAL_AUTH_FACEBOOK_KEY = '2261094383941531'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '50767d778053d85f5cf80574a2f3a8dd'  # App Secret

SOCIAL_AUTH_GITHUB_KEY = '9a49fd4678459ffb3de7'
SOCIAL_AUTH_GITHUB_SECRET = 'd04594c8a218e393b0ba0bc15c44e28b58660535'

LOGIN_URL = '/'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = '/'