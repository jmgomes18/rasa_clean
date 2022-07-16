from typing import Dict
from data.models import Fields
from abc import ABC, abstractclassmethod


class RegisterField(ABC):
    """Interface to RegisterField use case"""

    @abstractclassmethod
    def registry(
        cls, owner_id, title, description, active, type, order
    ) -> Dict[bool, Fields]:

        """Use case"""

        raise Exception("Should implment method: Registry")
