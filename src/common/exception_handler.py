from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from common.exceptions import CustomException, InternalServerError, ErrorDetail, InternalClientError
from common.responses import create_fail_response
from utils.log_utils import Logger


def custom_exception_handler(exc, context):
    # 예외 정보 로깅 강화
    Logger.error(f"Exception occurred: {exc}, Context: {context}")

    # CustomException 처리
    if isinstance(exc, CustomException):
        Logger.info(f"Handling CustomException: {exc.detail}")
        return create_fail_response(exc.detail)

    # DRF APIException 처리
    if isinstance(exc, APIException):
        Logger.info(f"Handling APIException: {exc.default_code} - {exc.detail}")
        return create_fail_response(ErrorDetail.build(exc.default_code, exc.detail, exc.status_code))

    # 상태 코드가 있는 일반 예외 처리 (4xx, 5xx)
    status_code = getattr(exc, "status_code", None)

    if status_code:
        error_detail = None
        if 400 <= status_code < 500:
            Logger.info(f"Client error occurred: {exc.detail}, Status Code: {status_code}")
            error_detail = InternalClientError(exc.detail, status_code).detail
        elif 500 <= status_code:
            Logger.error(f"Server error occurred: {exc.detail}, Status Code: {status_code}")
            error_detail = InternalServerError(exc.detail, status_code).detail

        if error_detail:
            return create_fail_response(error_detail)

    # DRF 기본 핸들러로 처리되지 않은 예외 처리
    response = exception_handler(exc, context)
    if response is not None:
        Logger.info(f"DRF exception handler response: {response.data}")
        return response

    # 처리되지 않은 예외에 대한 기본 응답
    Logger.error("Unhandled exception occurred")
    return create_fail_response(ErrorDetail.build("unhandled_error", "알 수 없는 오류가 발생했습니다.", 500))
