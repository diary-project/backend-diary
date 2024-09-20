from .base import *

SECRET_KEY = "django-insecure-nf+j=6s(uu+qu3_!x1y*)ho)*3dv@^4ebp7!thg-0*&%p4s9re"

DEBUG = True
ALLOWED_HOSTS = [
    "13.124.194.227",
    "ec2-13-124-194-227.ap-northeast-2.compute.amazonaws.com",
]

SERVER_URL = "http://13.124.194.227:8000"
CLIENT_REDIRECT_URL = "http://localhost:5173/oauth/kakao/callback/"

# DataBase
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME", "diary_db"),
        "USER": os.environ.get("DB_USER", "geuttaen"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "kJp#dpOFdJCADjLg8Z"),
        "HOST": os.environ.get(
            "DB_HOST", "diary-db-dev.c3e4cuegc63x.ap-northeast-2.rds.amazonaws.com"
        ),
        "PORT": "3306",
    }
}

# simplejwt setting
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
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
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# Celery Settings 추후에 별도 경로로 변경
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'
