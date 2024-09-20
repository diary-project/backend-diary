from rest_framework.views import exception_handler

from common.exceptions.error_codes import ErrorCode
from common.exceptions import CustomException
from common.responses import create_fail_response


def custom_exception_handler(exc, context):
    # CustomException을 처리하는 부분
    if isinstance(exc, CustomException):
        return create_fail_response(exc.error_code)

    # 기본 핸들러로 처리되지 않은 경우 DRF의 기본 핸들러를 사용
    response = exception_handler(exc, context)
    if response is not None:
        return response

    # 처리되지 않은 예외의 경우 기본 500 응답
    return create_fail_response(ErrorCode.INTERNAL_SERVER_ERROR)
