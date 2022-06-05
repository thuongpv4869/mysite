from config.settings.prod import *  # noqa: F403

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
    'drf_spectacular'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = [
    '172.19.0.1'
]

REST_FRAMEWORK.update({
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
})

SPECTACULAR_SETTINGS = {
    'TITLE': 'Mysite API',
    'DESCRIPTION': 'mysite tutorial',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
