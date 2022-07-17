from typing import List
from data.models import Fields
from abc import ABC, abstractmethod


class Fields(ABC):
    """Interface to FindUser use case"""

    @abstractmethod
    def insert_field(
        cls,
        id,
        owner_id,
        title,
        description,
        active,
        type,
        order,
        created_at,
        updated_at,
    ) -> Fields:
        """Insert Field"""

        raise NotImplementedError

    @abstractmethod
    def select(cls, field_id: str = None, active: bool = None) -> List[Fields]:
        """select fields"""
        raise NotImplementedError
