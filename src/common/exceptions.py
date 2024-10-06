from typing import Dict

from rest_framework import status


class ErrorDetail:
    def __init__(self, code: str, message: str, http_status_code: int):
        self._data = {
            "code": code,
            "message": message,
            "http_status_code": http_status_code,
        }

    @property
    def data(self) -> Dict:
        return self._data

    @classmethod
    def build(cls, code: str, message: str, http_status_code: int):
        return cls(code=code, message=message, http_status_code=http_status_code)


class CustomException(Exception):
    """
    CustomException
    - BaseErrorCode를 받아서 처리하는 예외 클래스
    """

    def __init__(self, code: str, message: str, http_status_code: int):
        self._code: str = code
        self._message: str = message
        self._http_status_code: int = http_status_code

    @property
    def detail(self) -> ErrorDetail:
        return ErrorDetail(self._code, self._message, self._http_status_code)


class InternalClientError(CustomException):
    def __init__(self, message: str, http_status_code: int):
        super().__init__("CLIENT_ERROR", message, http_status_code)


class InternalServerError(CustomException):
    def __init__(self, message: str, http_status_code: int):
        super().__init__("SERVER_ERROR", message, http_status_code)
