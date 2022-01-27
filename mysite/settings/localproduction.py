import os

# This is the custom settings file for the production stage in my private server
# This is to test the app's deployment status before pushing it all to Heroku
# The environment variables will still be taken from the .env file and Debug is set to true to see the potential errors

SECRET_KEY = os.environ.get('SECRET_KEY_PROD')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

# AWS S3 parameters
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = True # When files of the same name are uploaded, this will overwrite the previous file saved (I think this is better for me). so I have to be careful when uploading similar files if I don't want the previous one to be overwritten
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
