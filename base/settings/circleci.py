from .defaults import *

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

def show_toolbar(request):
    return False

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}