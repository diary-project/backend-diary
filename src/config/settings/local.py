from .base import *

SECRET_KEY = "hello-world"

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

SERVER_URL = "http://localhost:8000"
CLIENT_REDIRECT_URL = "http://localhost:3000/"

# DataBase
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

# simplejwt setting
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,  # 변경 필요 / 일단 임시로 SECRET_KEY
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "email",  # User Model에서 가져올 클래스 변수 명
    "USER_ID_CLAIM": "email",  # jwt에 USER_ID_FILED를 적용할 때 활용할 Key 값
    "SLIDING_TOKEN_LIFETIME": timedelta(hours=3),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}
