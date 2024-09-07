import logging


class Logger:
    _loggers = {}

    @classmethod
    def get_logger(cls):
        import inspect

        # 호출한 곳에서의 모듈 이름을 가져옴 (두 단계 위로 추적)
        module_name = inspect.stack()[2].frame.f_globals["__name__"]
        top_level_module = module_name.split(".")[0]

        if top_level_module not in cls._loggers:
            cls._loggers[top_level_module] = logging.getLogger(top_level_module)

        return cls._loggers[top_level_module]

    @classmethod
    def debug(cls, message, *args, **kwargs):
        cls.get_logger().debug(message, *args, **kwargs)

    @classmethod
    def info(cls, message, *args, **kwargs):
        cls.get_logger().info(message, *args, **kwargs)

    @classmethod
    def warning(cls, message, *args, **kwargs):
        cls.get_logger().warning(message, *args, **kwargs)

    @classmethod
    def error(cls, message, *args, **kwargs):
        cls.get_logger().error(message, *args, **kwargs)

    @classmethod
    def critical(cls, message, *args, **kwargs):
        cls.get_logger().critical(message, *args, **kwargs)

    # Python Logger에서는 Trace를 제공하지 않음... / 별도로 추가해서 사용해야 함
    # @classmethod
    # def trace(cls, message, *args, **kwargs):
    #     cls.get_logger().not_set(message, *args, **kwargs)
