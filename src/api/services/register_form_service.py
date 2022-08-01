from typing import Type
from domain.use_cases.interfaces.forms.register_form import RegisterForm
from api.presenters.errors import HttpErrors
from api.presenters.helpers import HttpRequest, HttpResponse


class RegisterFormService:
    """class to define register form service with its use cases"""

    def __init__(self, register_form_use_case: Type[RegisterForm]):
        self.register_form_use_case = register_form_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """implementing form service"""

        response = None
        if not http_request.body:
            https_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=https_error["statusCode"], body=https_error["body"]
            )

        body_params = http_request.body

        if "form" in body_params.keys():
            owner_id = body_params["form"]["owner_id"]
            title = body_params["form"]["title"]
            description = body_params["form"]["description"]
            active = body_params["form"]["active"]
            response = self.register_form_use_case.registry(
                owner_id, title, description, active
            )

        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            https_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=https_error["statusCode"], body=https_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
