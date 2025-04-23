
from .main import *

print('settings.main.py - enabled')

try:
    from .local import *
    print('settings.local.py - enabled')
except ImportError:
    from .environ import *
    print('settings.environ.py - enabled')

if DEBUG:
    print('Debug view environments vars:')
    print(f'    DEBUG: {DEBUG}')
    print(f'    SECRET_KEY: {SECRET_KEY}')
    print(f'    ALLOWED_HOSTS: {ALLOWED_HOSTS}')
    print(f'    DATABASES: {DATABASES}')
