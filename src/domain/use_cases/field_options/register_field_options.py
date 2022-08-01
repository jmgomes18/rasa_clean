from typing import Type, Dict, List
from domain.use_cases.fields.select_field import SelectField
from infra.repositories.interfaces import FieldOptions as RepositoryInterface
from domain.use_cases.interfaces.field_options.register_field_options import (
    RegisterFieldOptions as Interface,
)
from data.models import FieldOptions, Fields


class RegisterFieldOptions(Interface):
    """class to define Register Field"""

    def __init__(
        self,
        field_options_repository: Type[RepositoryInterface],
        select_field: Type[SelectField],
    ):
        self.field_options_repository = field_options_repository
        self.select_field = select_field

    def registry(
        self, name: str, value: str, field_information
    ) -> Dict[bool, FieldOptions]:

        response = None

        validate_entry = isinstance(name, str) and isinstance(value, str)

        field = self.__find_field_information(field_information)
        checker = validate_entry and field["Success"]

        if checker:
            response = self.field_options_repository.insert_field_options(
                name, value, field_information["field_id"]
            )

        return {"Success": "true", "Data": response}

    def __find_field_information(self, field_information) -> Dict[bool, List[Fields]]:
        """Check field Infos and select field
        :param - field_information: Dictionary with field_id and/or field active status
        :return - Dictionary with the response of select_field use case
        """

        field = None
        field_params = field_information.keys()

        if "field_information" in field_params and "active" in field_params:
            field = self.select_field.by_id_and_active(
                field_information["field_id"], field_information["active"]
            )

        elif "field_id" not in field_params and "active" in field_params:
            field = self.select_field.by_active(field_information["active"])

        elif "field_id" in field_params and "active" not in field_params:
            field = self.select_field.by_id(field_information["field_id"])

        else:
            return {"Success": False, "Data": None}

        return field
