import os

# This is the custom settings file for the production stage in Heroku
# The environment variables will no longer be taken from the .env file but from Heroku's environment settings

SECRET_KEY = os.environ.get('SECRET_KEY_PROD')
DEBUG = True
ALLOWED_HOSTS = ['www.jordantanudjaja.com', 'jordantanudjaja.com']

# AWS S3 parameters
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = True # When files of the same name are uploaded, this will overwrite the previous file saved (I think this is better for me). so I have to be careful when uploading similar files if I don't want the previous one to be overwritten
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# HTTPS settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
