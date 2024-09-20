from rest_framework import status
from common.exceptions import CustomException


class DiaryNotFoundException(CustomException):
    def __init__(self):
        super().__init__(
            "DIARY_ERROR_001", "조회된 일기가 없습니다.", status.HTTP_404_NOT_FOUND
        )
