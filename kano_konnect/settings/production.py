from base import *



# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "ec2-54-228-139-57.eu-west-1.compute.amazonaws.com", "connect.ehealth.org.ng"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_setting('SECRET_KEY')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = '/var/kano_konnect_media'  ## Vernon