''' local.py is supposed to be ignored while pushing into your repo but I have left it as it is for refrence purpose '''

from .base import *

DATABASES={

   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insight',
        'USER': 'postgres',
        'PASSWORD': 'x',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}