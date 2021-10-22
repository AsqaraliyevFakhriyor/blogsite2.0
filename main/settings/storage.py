import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


USE_S3 = "<TRUE IF YOU WANT TO USE AWS BUCKET ELSE IT WILL RUN LOCALLY>"

if USE_S3:
# Boto3
    AWS_QUERYSTRING_AUTH = False
    # AWS
    AWS_ACCESS_KEY_ID = "<AMAZON USER ACCESS KEY ID>"
    AWS_SECRET_ACCESS_KEY = "<AMAZON USER SECRET ACCESS KEY>"
    AWS_STORAGE_BUCKET_NAME = "<AMAZON S3 BUCKET NAME>"
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # static files storages
    STATICFILES_STORAGE = 'main.settings.StaticStorage'
    # A path prefix that will be prepended to all uploads
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

    # public media storage
    DEFAULT_FILE_STORAGE = 'main.settings.MediaStorage'
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'

    CKEDITOR_BASEPATH = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/ckeditor/ckeditor/"

    

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Identify our Media files
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Ckeditor config
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

CKEDITOR_UPLOAD_PATH = f"{MEDIA_URL}uploads/"
CKEDITOR_RESTIRCT_BY_USER = True

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)