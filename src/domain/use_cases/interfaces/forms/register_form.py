from typing import Dict
from data.models import Forms
from abc import ABC, abstractclassmethod


class RegisterForm(ABC):
    """Interface to RegisterField use case"""

    @abstractclassmethod
    def registry(cls, owner_id, title, description, active) -> Dict[bool, Forms]:

        """Use case"""

        raise NotImplementedError("Should implment method: Registry")
