from typing import Type, Dict
from infra.repositories.interfaces import Fields as RepositoryInterface
from domain.use_cases.interfaces.fields.register_field import RegisterField
from data.models import Fields


class RegisterField(RegisterField):
    """class to define Register Field"""

    def __init__(self, field_repository: Type[RepositoryInterface]):
        self.field_repository = field_repository

    def registry(
        self,
        owner_id: str,
        title: str,
        description: str,
        active: bool,
        type: str,
        order: int,
    ) -> Dict[bool, Fields]:

        response = None

        # Validating entry and trying to find an user
        validate_entry = (
            isinstance(owner_id, str)
            and isinstance(title, str)
            and isinstance(description, str)
            and isinstance(active, bool)
            and isinstance(type, str)
            and isinstance(order, int)
        )

        if validate_entry:
            response = self.field_repository.insert_field(
                owner_id, title, description, active, type, order
            )

        return {"Success": "true", "Data": response}
