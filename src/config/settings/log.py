# settings.py

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,  # 기존 로거 비활성화 여부
    "formatters": {  # 로그 형식 설정
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {  # 로그를 출력할 핸들러 설정
        "console": {  # 콘솔에 출력
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",  # 형식을 simple로 변경 가능
        },
    },
    "loggers": {  # 로거 설정
        "django": {  # Django 관련 로깅
            "handlers": ["console"],  # 콘솔에만 로그 출력
            "level": "INFO",
            "propagate": True,
        },
        "diary": {  # 특정 앱의 로깅
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "image": {  # 특정 앱의 로깅
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "tag": {  # 특정 앱의 로깅
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "oauth": {  # 특정 앱의 로깅
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "utils": {  # 특정 앱의 로깅
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
