from base import *

# This defaults to no key, don't use in production!
#SECRET_KEY = get_env_setting('SECRET_KEY',)
SECRET_KEY = 'ev&6==8*f-gjgw^#mk%+5t*7if*4z73spk=w!iq*0k5re$rqf'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}