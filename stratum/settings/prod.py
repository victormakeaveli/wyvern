import os
from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, './static/files')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
