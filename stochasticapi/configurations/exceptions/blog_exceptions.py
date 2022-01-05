from rest_framework.response import Response
from rest_framework.views import exception_handler

from stochasticapi.configurations.utilities.http_codes import BAD_REQUEST
from ..utilities.api_response import BlogResponse

_ERROR_MESSAGE = "A server error has occurred."
_TOKEN_INVALID_STATUS_CODE = 401


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:

        response = __transform_error(response)

    else:
        response = Response(status=BAD_REQUEST)
        response.data = BlogResponse(
            http_status=BAD_REQUEST,
            message=_ERROR_MESSAGE,
            data={"errors": [{"detail": str(exc)}]},
            success=False,
            code='00',
        ).format_response()

    return response


def __transform_error(response):
    data = response.data
    response.data = {}

    error_format = []
    error_keys = set(["http_status"])
    error_data_keys = set(list(data.keys()))

    error_format = {"errors": []}

    # Manually raised exceptions
    if error_keys.intersection(error_data_keys):
        error_format["errors"].append(data["data"])
        data["data"] = error_format
        response.data = data
        response.status_code = int(response.data["http_status"])
    # System raised exceptions
    else:
        for field, value in data.items():
            if response.status_code == _TOKEN_INVALID_STATUS_CODE:
                # Handle system raised token invalid errors only
                if isinstance(value, str):
                    error_format["errors"].append({field: "".join(value)})
            else:
                if type(value) is list:
                    for val in value:
                        if type(val) is dict:
                            for k, v in val.items():
                                error_format["errors"].append(
                                    {field: "".join(v)}
                                )
                        else:
                            error_format["errors"].append(
                                {field: "".join(value)}
                            )
                else:
                    error_format["errors"].append({field: "".join(value)})

        response.data = BlogResponse(
            http_status=response.status_code,
            message=_ERROR_MESSAGE,
            data=error_format,
            success=False,
            code='00',
        ).format_response()

    return response