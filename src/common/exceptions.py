from enum import Enum
from rest_framework.exceptions import APIException


class BaseErrorCode(Enum):
    ...


class BaseAPIException(APIException):
    status_code = 500

    def __init__(self, error_code: BaseErrorCode):
        super().__init__(
            code=error_code.name,
            detail=error_code.value
        )

    @classmethod
    def get_status_code(cls):
        return cls.status_code
