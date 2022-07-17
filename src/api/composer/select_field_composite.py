from api.services.select_field_service import SelectFieldService
from domain.use_cases.fields.select_field import SelectField
from infra.repositories.fields.field_repository import FieldRepository


def select_field_composer() -> SelectFieldService:
    """Composing Register User Route
    :param - None
    :return - Object with Register User Route
    """

    repository = FieldRepository()
    use_case = SelectField(repository)
    select_field_route = SelectFieldService(use_case)

    return select_field_route
