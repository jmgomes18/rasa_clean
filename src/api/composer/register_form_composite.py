from api.services.register_form_service import RegisterFormService
from domain.use_cases.forms.register_form import RegisterForm
from infra.repositories.forms.form_repository import FormRepository


def register_form_composer() -> RegisterFormService:
    """Composing Register Formd Route
    :param - None
    :return - Object with Register User Route
    """

    repository = FormRepository()
    use_case = RegisterForm(repository)
    register_field_route = RegisterFormService(use_case)

    return register_field_route
