"""
Django settings for p_notification_rapi project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv


# reading .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False if os.getenv("MODE").lower() == "PROD" else os.getenv("DJANGO_DEBUG")
DEBUG = int(os.environ.get("DJANGO_DEBUG", default=1))

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS")

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'import_export',
    'multi_captcha_admin',
    'admin_honeypot',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'debug_toolbar',
    'defender',
    'lockdown',
    'loginas',
    'cuser',
    # Your APPS GOES HERE
    'a_template',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'defender.middleware.FailedLoginMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'lockdown.middleware.LockdownMiddleware',
    # Your Middleware Goes Here
]

ROOT_URLCONF = 'p_notification_rapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'p_notification_rapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


if os.getenv("USING_DB").lower() == "sql":

    #SQLITE DB
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("SQL_ENGINE"),
            'NAME': BASE_DIR / os.getenv("SQL_DATABASE"),
        }
    }

else:

    # POSTGRESQL DB
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("PSQL_ENGINE"),
            'NAME': os.getenv("PSQL_DATABASE"),
            'USER': os.getenv("PSQL_USER"),
            'PASSWORD': os.getenv("PSQL_PASSWORD"),
            'HOST': os.getenv("PSQL_HOST"),
            'PORT': os.getenv("PSQL_PORT"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# django-multi-captcha-admin

RECAPTCHA_PUBLIC_KEY = '6LezSCkaAAAAALMUu8hYbouPm1NJoqQ-XPWP-W9r'
RECAPTCHA_PRIVATE_KEY = '6LezSCkaAAAAAEuo9LxLmMSjSDu8ZmhFI8bqAWBH'

MULTI_CAPTCHA_ADMIN = {
    'engine': 'recaptcha2',
}

# django-debug-toolbar

# The Debug Toolbar is shown only if your IP address is listed in the INTERNAL_IPS setting.

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

DEFENDER_COOLOFF_TIME = 600 # seconds

# django-lockdown

if os.getenv("LOCKDOWN_PASSWORDS"):
    LOCKDOWN_PASSWORDS = tuple(os.getenv("LOCKDOWN_PASSWORDS").split(" "))


LOCKDOWN_ENABLED = os.getenv("LOCKDOWN_ENABLED", False)

#django-object-tools
SERIALIZATION_MODULES = {
    'csv': 'export.serializers.csv_serializer'
}

#django-admin-interface
X_FRAME_OPTIONS='SAMEORIGIN'


#django-loginas

# This will only allow admins to log in as other users:
CAN_LOGIN_AS = lambda request, target_user: request.user.is_superuser

#django-import-export
IMPORT_EXPORT_USE_TRANSACTIONS = True

#django-username-email 
AUTH_USER_MODEL = 'cuser.CUser'
