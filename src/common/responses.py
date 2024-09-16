from rest_framework.response import Response
from rest_framework.status import *


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR

from common.exceptions.error_codes import BaseErrorCode


class CustomResponse(Response):
    def __init__(self, data=None, code="SUCCESS", message=None, http_status_code=HTTP_200_OK, **kwargs):
        if 400 <= http_status_code < 500:
            status = "EXCEPTION"
        elif http_status_code >= 500:
            status = "ERROR"
        else:
            status = "SUCCESS"

        response_data = {
            "status": status,
            "code": code,
            "data": data if status == "SUCCESS" else None,
            "message": message if status != "SUCCESS" else None
        }

        super().__init__(data=response_data, status=http_status_code, **kwargs)


def create_success_response(data=None, status=HTTP_200_OK, **kwargs):
    return CustomResponse(
        data=data,
        http_status_code=status,
        **kwargs
    )


def create_fail_response(error_code: BaseErrorCode, **kwargs):
    return CustomResponse(
        **error_code.error_detail,
        **kwargs
    )

# class SuccessResponse(Response):
#     def __init__(
#             self,
#             data: object = None,
#             status: int = HTTP_200_OK,
#             *args,
#             **kwargs
#     ):
#         response_data = {
#             "status": "SUCCESS",
#             "code": status,
#             "data": data,
#         }
#
#         super().__init__(data=response_data, status=status, *args, **kwargs)
#
#
# class ErrorResponse(Response):
#     def __init__(
#             self,
#             code: str = "ERROR",
#             message: str = "Internal Server Error",
#             http_status_code: int = HTTP_500_INTERNAL_SERVER_ERROR,
#             *args,
#             **kwargs
#     ):
#         status = "ERROR"
#         if 400 <= http_status_code < 500:
#             status = "EXCEPTION"
#
#         response_data = {
#             "status": status,
#             "code": code,
#             "data": None,
#             "message": message
#         }
#
#         super().__init__(data=response_data, *args, **kwargs)

