from common.exceptions.error_codes import BaseErrorCode


class CustomException(Exception):
    """
    CustomException
    - BaseErrorCode를 받아서 처리하는 예외 클래스
    """

    def __init__(self, error_code: BaseErrorCode):
        """
        :param error_code: BaseErrorCode Enum의 인스턴스를 받습니다.
        """
        self.error_code = error_code
