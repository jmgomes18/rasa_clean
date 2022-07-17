from typing import Type, Dict, List
from infra.repositories.interfaces.fields import Fields as RepositoryInterface
from data.models import Fields
from domain.use_cases.interfaces.fields.select_field import (
    SelectField as SelectFieldInterface,
)


class SelectField(SelectFieldInterface):
    """implementing Select fields use cases"""

    def __init__(self, field_repository: Type[RepositoryInterface]):
        self.field_repository = field_repository

    def by_id(self, field_id: str) -> Dict[bool, List[Fields]]:
        response = None
        validate_entry = isinstance(field_id, str)

        if validate_entry:
            response = self.field_repository.select(field_id=field_id)

        return {"Success": validate_entry, "Data": response}

    def by_active(self, active: bool) -> Dict[bool, List[Fields]]:
        response = None
        if active == "True":
            response = self.field_repository.select(active=True)
        else:
            response = self.field_repository.select(active=False)

        return {"Success": True, "Data": response}

    def by_id_and_active(self, field_id: int, active: str) -> Dict[bool, List[Fields]]:
        response = None
        validate_entry = isinstance(active, bool) and isinstance(field_id, str)

        if validate_entry:
            response = self.field_repository.select(field_id=field_id, active=active)

        return {"Success": validate_entry, "Data": response}
