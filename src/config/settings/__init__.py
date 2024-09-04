import os
from .base import *

env = os.getenv('DJANGO_ENV')

if env == 'dev':
    from .dev import *
else:
    from .local import *
