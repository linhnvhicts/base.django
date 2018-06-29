from .circleci import *

# https://devcenter.heroku.com/articles/django-assets#whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'