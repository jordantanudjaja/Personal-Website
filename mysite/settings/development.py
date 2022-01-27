import os

# This is the custom settings file for the development stage in my private server

SECRET_KEY = os.environ.get('SECRET_KEY_DEV')
DEBUG = True
