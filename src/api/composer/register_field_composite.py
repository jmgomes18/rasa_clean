from api.services.fields import RegisterFieldService
from domain.use_cases.fields.register_field import RegisterField
from infra.repositories.fields.field_repository import FieldRepository


def register_field_composer() -> RegisterFieldService:
    """Composing Register User Route
    :param - None
    :return - Object with Register User Route
    """

    repository = FieldRepository()
    use_case = RegisterField(repository)
    register_field_route = RegisterFieldService(use_case)

    return register_field_route
