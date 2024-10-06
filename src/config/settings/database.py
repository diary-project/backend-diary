from .base import *
from os import getenv

env_path = os.path.join(BASE_DIR, "resources", "envs", ".env")
env = Config(RepositoryEnv(env_path))

django_env = getenv("DJANGO_ENV")
CACHE_TIMEOUT = env("CACHE_TIMEOUT", cast=int)

# DataBase
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "diary-mem-cache",  # 여러 인스턴스에서 구분되는 유니크한 이름
    }
}

if django_env == "dev":
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
    # CACHE
    CACHES = {
        # "default": {
        #     "BACKEND": "django_redis.cache.RedisCache",
        #     "LOCATION": f"redis://{env("CACHE_HOST")}:{env("CACHE_PORT")}/1",
        #     "OPTIONS": {
        #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
        #         "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",  # 캐시 압축
        #     },
        # }
        # settings.py
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "diary-mem-cache",  # 여러 인스턴스에서 구분되는 유니크한 이름
        }
    }
