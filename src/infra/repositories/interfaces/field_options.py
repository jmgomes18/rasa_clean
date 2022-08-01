from data.models import FieldOptions
from abc import ABC, abstractmethod


class FieldOptions(ABC):
    """Interface to FindUser use case"""

    @abstractmethod
    def insert_field_options(
        cls,
        id,
        name,
        value,
        created_at,
        updated_at,
    ) -> FieldOptions:
        """Insert Field"""

        raise NotImplementedError
