import json
from typing import Type
from domain.use_cases.interfaces.fields.register_field import RegisterField
from api.presenters.errors import HttpErrors
from api.presenters.helpers import HttpRequest, HttpResponse


class RegisterFieldService:
    """class to define register field service with its use cases"""

    def __init__(self, register_field_use_case: Type[RegisterField]):
        self.register_field_use_case = register_field_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """implementing field service"""

        response = None
        if http_request.body not in http_request:
            https_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=https_error["statusCode"], body=https_error["body"]
            )

        body_params = json.loads(http_request.body)

        if "field" in body_params.keys():
            owner_id = body_params["field"]["owner_id"]
            title = body_params["field"]["title"]
            description = body_params["field"]["description"]
            active = body_params["field"]["active"]
            type = body_params["field"]["type"]
            order = body_params["field"]["order"]
            response = self.register_field_use_case.registry(
                owner_id, title, description, active, type, order
            )

        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            https_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=https_error["statusCode"], body=https_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
