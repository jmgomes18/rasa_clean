from typing import Dict, List
from data.models import Fields
from abc import ABC, abstractclassmethod


class SelectField(ABC):
    """Interface to FindPet use case"""

    @abstractclassmethod
    def by_id(self, field_id: str) -> Dict[bool, List[Fields]]:
        raise NotImplementedError

    @abstractclassmethod
    def by_active(self, active: bool) -> Dict[bool, List[Fields]]:
        raise NotImplementedError

    @abstractclassmethod
    def by_id_and_active(self, field_id: int, active: str) -> Dict[bool, List[Fields]]:
        raise NotImplementedError
