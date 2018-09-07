from .settings import *


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "myanalyzer/assets"),
]
# STATIC_ROOT = os.path.join(BASE_DIR, "myanalyzer/assets")

WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json'),
        }
}