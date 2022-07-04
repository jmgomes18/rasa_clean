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
    ):
        """Insert Field"""

        raise Exception("Should implement method: by_field_id")
