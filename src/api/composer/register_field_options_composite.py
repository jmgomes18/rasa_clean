from api.services.register_field_options_service import RegisterFieldOptionsService
from domain.use_cases.field_options.register_field_options import RegisterFieldOptions
from infra.repositories.field_options.field_options_repository import (
    FieldOptionsRepository,
)
from infra.repositories.fields.field_repository import FieldRepository
from domain.use_cases.fields.select_field import SelectField


def register_field_options_composer() -> RegisterFieldOptionsService:
    """Composing Register User Route
    :param - None
    :return - Object with Register User Route
    """

    repository = FieldOptionsRepository()
    find_field = SelectField(FieldRepository())
    use_case = RegisterFieldOptions(repository, find_field)
    register_field_route = RegisterFieldOptionsService(use_case)

    return register_field_route
