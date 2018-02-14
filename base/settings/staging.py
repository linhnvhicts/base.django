### staging.py
from .defaults import *
import os
import dj_database_url


print("Running with settings: {0}".format("Staging Environment"))

DEBUG = True
### other production-specific stuff

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# https://devcenter.heroku.com/articles/django-assets
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
