"""
Settings file for local development
"""
from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0',
                 'web', 'db', 'redis', 
                 'celery', 'testserver']

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    )
}

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']
