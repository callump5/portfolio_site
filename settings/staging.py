from base import *

DEBUG = False

#Live
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

SITE_URL = ['cpullinger.herokuapp.com',
    'www.callum-pullinger.co.uk']

ALLOWED_HOSTS.append(
    'cpullinger.herokuapp.com',
    'www.callum-pullinger.co.uk')


# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}