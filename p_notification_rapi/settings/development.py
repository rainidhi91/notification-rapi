from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DJANGO_DEBUG", default=1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", '*').split(" ")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.getenv("USING_DB").lower() == "sql":

    #SQLITE DB
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("SQL_ENGINE"),
            'NAME': str(os.path.join(BASE_DIR , os.getenv("SQL_DATABASE"))),
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


