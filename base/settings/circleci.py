from .defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',
        'USER': 'root',
        'PASSWORD': 'rootpw',
        'HOST': '127.0.0.1',
    }
}
