### dev.py
from .defaults import *

print("Running with settings: {0}".format("Development Environment"))

DEBUG = True
### other development-specific stuff
LANGUAGE_CODE = 'en-us'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'base.django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}