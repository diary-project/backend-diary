from .base import *
from .database import *
from .swagger import *
from .log import *
from os import getenv


env = getenv("DJANGO_ENV")

if env == "dev":
    from .dev import *
else:
    from .local import *
