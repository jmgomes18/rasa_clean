from typing import Type, Dict
from src.data.repositories.interfaces import Fields as RepositoryInterface
from src.domain.interfaces.fields import register_field
from src.data.models import Fields


class RegisterField(register_field.RegisterField):
    """class to define Register Field"""

    def __init__(self, field_repository: Type[RepositoryInterface]):
        self.field_repository = field_repository

    def registry(
        self, owner_id, title, description, active, type, order
    ) -> Dict[bool, Fields]:

        response = None

        # Validating entry and trying to find an user

        response = self.field_repository.insert_field(
            owner_id, title, description, active, type, order
        )

        return {"Success": "true", "Data": response}
