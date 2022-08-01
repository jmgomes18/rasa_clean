from typing import Type
from domain.use_cases.interfaces.field_options.register_field_options import (
    RegisterFieldOptions as UseCase,
)
from api.presenters.errors import HttpErrors
from api.presenters.helpers import HttpRequest, HttpResponse


class RegisterFieldOptionsService:
    """class to define register field service with its use cases"""

    def __init__(self, use_case: Type[UseCase]):
        self.use_case = use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """implementing field service"""

        response = None
        if not http_request.body:
            https_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=https_error["statusCode"], body=https_error["body"]
            )

        body_params = http_request.body

        if "options" in body_params.keys():
            name = body_params["options"]["name"]
            value = body_params["options"]["value"]
            response = self.use_case.registry(name, value, http_request.path_params)

        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            https_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=https_error["statusCode"], body=https_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
