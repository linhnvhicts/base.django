from .defaults import *

# https://devcenter.heroku.com/articles/django-assets#whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)