import os
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY_PROD')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'jordantanudjaja.herokuapp.com']

# Postgres Database to be submitted in Heroku
DATABASES = {   # Taken from base.py
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env) # Updating DATABASES to include the Postgres database set to me by Heroku

# AWS S3 parameters
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = True # When files of the same name are uploaded, this will overwrite the previous file saved (I think this is better for me). so I have to be careful when uploading similar files if I don't want the previous one to be overwritten
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # HTTPS settings
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# #
# # # HSTS settings
# SECURE_HSTS_SECONDS = 31536000 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

django_heroku.settings(locals()) # For my website to talk to Production Postgres database
