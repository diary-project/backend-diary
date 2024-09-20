from rest_framework import status
from common.exceptions import CustomException


class DiaryNotFoundException(CustomException):
    def __init__(self):
        super().__init__(
            "DIARY_ERROR_001", "조회된 일기가 없습니다.", status.HTTP_404_NOT_FOUND
        )


class MultipleDiariesFoundException(CustomException):
    def __init__(self):
        super().__init__(
            "DIARY_ERROR_002",
            "여러 개의 일기가 발견되었습니다.",
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
