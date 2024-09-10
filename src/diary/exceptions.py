from rest_framework import status

from common.exceptions import BaseAPIException, BaseErrorCode


class DiaryErrorCode(BaseErrorCode):
    DIARY_NOT_FOUND = "조회된 일기가 없습니다."


class DiaryNotFoundException(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, error_code: DiaryErrorCode = DiaryErrorCode.DIARY_NOT_FOUND):
        super().__init__(error_code=error_code)
