from .base import*


DEBUG = False

ADMINS = {
            ('Boris Szelcsanyi', 'boris.szelcsanyi@student.unisg.ch')   
        }

ALLOWED_HOSTS = ['*']

DATABASES = {
        'default' : {
            'ENGINE' : 'django.db.backends.postgresql_psycopg2',
            'NAME' : 'production',
            'USER' : 'postgres',
            'PASWORD' : '',

         }
     }

