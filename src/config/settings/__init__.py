import os
from .base import *
from .swagger import *
from .log import *

env = os.getenv("DJANGO_ENV")

if env == "dev":
    from .dev import *
else:
    from .local import *
