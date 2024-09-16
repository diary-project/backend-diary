from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND
from common.exceptions.error_codes import BaseErrorCode
from common.exceptions.exceptions import CustomException


class DiaryErrorCode(BaseErrorCode):
    DIARY_NOT_FOUND = ("조회된 일기가 없습니다.", HTTP_404_NOT_FOUND)


class DiaryNotFoundException(CustomException):
    pass
