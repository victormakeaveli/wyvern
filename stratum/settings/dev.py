import os
from .base import *

SECRET_KEY = '2^!d=*%=a@nn4+mb1ff(*yu5$4dej1apm3*6%%89csmc@hw(nv'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, './static_files')
    
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, './static'),
]

