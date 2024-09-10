from rest_framework.response import Response
from rest_framework.status import *


class SuccessResponse(Response):
    def __init__(
            self,
            data: object = None,
            http_status_code: int = HTTP_200_OK,
            *args,
            **kwargs
    ):
        response_data = {
            "status": "SUCCESS",
            "code": http_status_code,
            "data": data,
        }

        super().__init__(data=response_data, status=http_status_code, *args, **kwargs)


class ErrorResponse(Response):
    def __init__(
            self,
            code: str = "ERROR",
            message: str = "Internal Server Error",
            http_status_code: int = HTTP_500_INTERNAL_SERVER_ERROR,
            *args,
            **kwargs
    ):
        status = "ERROR"
        if 400 <= http_status_code < 500:
            status = "EXCEPTION"

        response_data = {
            "status": status,
            "code": code,
            "data": None,
            "message": message
        }

        super().__init__(data=response_data, *args, **kwargs)
