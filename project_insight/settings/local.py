''' local.py is supposed to be ignored while pushing into your repo but I have left it as it is for refrence purpose '''

from .base import *
import os 
from decouple import config

DATABASES={

   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insight',
        'USER': 'postgres',
        'PASSWORD': config('password'),
        'HOST': 'localhost',
        'PORT': '5432',

    }
}


STATICFILES_DIRS = [os.path.join(BASE_DIR, '../static')]