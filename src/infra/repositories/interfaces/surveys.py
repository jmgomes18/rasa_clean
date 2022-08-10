from typing import List
from data.models import Surveys
from abc import ABC, abstractmethod


class Surveys(ABC):
    """Interface to FindUser use case"""

    @abstractmethod
    @classmethod
    def insert_survey(
        cls, owner_id, value: str, status: str, author_id, time_elapsed
    ) -> Surveys:

        raise NotImplementedError

    @abstractmethod
    def select(cls, field_id: str = None, status: bool = None) -> List[Surveys]:
        """select Surveys"""
        raise NotImplementedError
