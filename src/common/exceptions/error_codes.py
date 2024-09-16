from enum import Enum
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR


class BaseErrorCode(Enum):
    INTERNAL_SERVER_ERROR = ("정의된 예외가 없습니다.", HTTP_500_INTERNAL_SERVER_ERROR)

    def __init__(self, message: str, http_status_code: int):
        self.message: str = message
        self.http_status_code: int = http_status_code

    @property
    def error_detail(self):
        """
        에러 코드, 메시지, 상태 코드를 한꺼번에 반환합니다.
        """
        return {
            "code": self.name,
            "message": self.message,
            "http_status_code": self.http_status_code
        }
