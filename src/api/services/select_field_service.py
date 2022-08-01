from typing import Type
from api.services.service_interface import RouteInterface
from domain.use_cases.interfaces.fields.select_field import SelectField
from api.presenters.errors import HttpErrors
from api.presenters.helpers import HttpRequest, HttpResponse


class SelectFieldService(RouteInterface):
    """class to define register field service with its use cases"""

    def __init__(self, select_field_use_case: Type[SelectField]):
        self.select_field_use_case = select_field_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "field_id" in query_string_params and "active" in query_string_params:
                field_id = http_request.query["field_id"]
                active = http_request.query["active"]
                response = self.select_field_use_case.by_id_and_active(
                    field_id=field_id, active=active
                )

            elif (
                "field_id" in query_string_params
                and "active" not in query_string_params
            ):
                field_id = http_request.query["field_id"]
                response = self.select_field_use_case.by_id(field_id=field_id)

            elif (
                "field_id" not in query_string_params
                and "active" in query_string_params
            ):
                active = http_request.query["active"]
                response = self.select_field_use_case.by_active(active=active)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["statusCode"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["statusCode"], body=http_error["body"]
        )
