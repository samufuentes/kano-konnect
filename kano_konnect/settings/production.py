from base import *



# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "54.220.157.69", "connect.ehealth.org.ng"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_setting('SECRET_KEY')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = '/var/kano_konnect_media'  ## Vernon

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kano_konnect',
        'USER': 'postgres',
        'PASSWORD': get_env_setting('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}