from .base import *


DEBUG = False

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xxx',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': 'xxx.xxx.xxx.rds.amazonaws.com',
        'PORT': '5432',
    }
}

AWS_ACCESS_KEY_ID = 'xxx'
AWS_SECRET_ACCESS_KEY = 'xxx'
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'aws_storage_classes.MediaStorage'
STATICFILES_STORAGE = 'aws_storage_classes.StaticStorage'

AWS_STORAGE_BUCKET_NAME = 'xxx'
AWS_S3_DOMAIN = 's3://s3-us-west-2.s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME

STATIC_URL = AWS_S3_DOMAIN + '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = AWS_S3_DOMAIN + '/media/'
