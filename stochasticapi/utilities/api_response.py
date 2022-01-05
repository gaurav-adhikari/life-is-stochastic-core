from stochasticapi.utilities.http_codes import OK
from rest_framework.response import Response


class BlogResponse:
    def __init__(
        self, http_status=OK, message=None, data=None, success=True, code=None
    ):
        self.__http_status = http_status
        self.__message = message
        self.__data = data
        self.__success = success
        self.__error_code = code

    def build_response(self):
        return Response(self.format_response(), content_type="application/json")

    def format_response(self):
        return {
            "http_status": self.__http_status,
            "message": self.__message,
            "data": self.__data,
            "success": self.__success,
            "code": self.__error_code
        }