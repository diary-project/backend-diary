from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from common.exceptions import ErrorDetail


class CustomResponse(Response):
    def __init__(self, data=None, code="SUCCESS", message=None, http_status_code=HTTP_200_OK, **kwargs):
        status = self._get_status(http_status_code)

        response_data = {
            "status": status,
            "code": code,
            "data": data if status == "SUCCESS" else None,
            "message": message if status != "SUCCESS" else None,
        }

        super().__init__(data=response_data, status=http_status_code, **kwargs)

    @staticmethod
    def _get_status(http_status_code: int) -> str:
        """HTTP 상태 코드에 따른 응답 상태 결정"""
        if 400 <= http_status_code < 500:
            return "EXCEPTION"
        elif http_status_code >= 500:
            return "ERROR"
        return "SUCCESS"


def create_success_response(data=None, status=HTTP_200_OK, **kwargs):
    return CustomResponse(data=data, http_status_code=status, **kwargs)


def create_fail_response(error_detail: ErrorDetail, **kwargs):
    return CustomResponse(**error_detail.data, **kwargs)
