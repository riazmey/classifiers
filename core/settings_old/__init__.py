
from .main import *
from .environ import *

#try:
#    from .local import *
#except ImportError:
#    from .environ import *

if DEBUG:
    print('Debug view environments vars:')
    print(f'    DEBUG: {DEBUG}')
    print(f'    SECRET_KEY: {SECRET_KEY}')
    print(f'    ALLOWED_HOSTS: {ALLOWED_HOSTS}')
    print(f'    DATABASES: {DATABASES}')
