from typing import Type
from src.domain.interfaces.fields import register_field
from src.api.presenters.errors import HttpErrors
from src.api.presenters.helpers import HttpRequest, HttpResponse


class RegisterFieldService:
    def __init__(self, register_field_use_case: Type[register_field.RegisterField]):
        self.register_field_use_case = register_field_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """implementing field service"""

        response = None

        if http_request.body not in http_request:
            https_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=https_error["status_code"], body=https_error["body"]
            )

        owner_id = http_request["owner_id"]
        title = http_request["title"]
        description = http_request["description"]
        active = http_request["active"]
        type = http_request["type"]
        order = http_request["order"]

        response = self.register_field_use_case.insert_field(
            owner_id, title, description, active, type, order
        )

        return HttpResponse(status_code=200, body=response["Data"])
