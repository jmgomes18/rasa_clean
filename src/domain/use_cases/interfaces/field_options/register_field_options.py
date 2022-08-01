from typing import Dict
from data.models import FieldOptions
from abc import ABC, abstractclassmethod


class RegisterFieldOptions(ABC):
    """Interface to RegisterField use case"""

    @abstractclassmethod
    def registry(cls, name, value, field_id) -> Dict[bool, FieldOptions]:

        """Use case"""

        raise NotImplementedError("Should implment method: Registry")
