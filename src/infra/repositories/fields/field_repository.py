import uuid
from datetime import datetime
from infra.repositories.interfaces import Fields as Interface
from data.models.fields import Fields
from infra.config import DBConnectionHandler
from infra.entities import Fields as FieldModel


class FieldRepository(Interface):
    """Field Repository"""

    @classmethod
    def insert_field(
        cls,
        owner_id: uuid,
        title: str,
        description: str,
        active: bool,
        type: str,
        order: int,
    ) -> Fields:
        """
        Insert data in Fields entity
        :param - self
                - owner_id
                - title
                - description
                - active
                - type
                - order
                - created_at
                - updated_at
        :return - tuple with new field inserted
        """

        with DBConnectionHandler() as db_conn:
            try:
                new_field = FieldModel(
                    id=uuid.uuid4(),
                    owner_id=owner_id,
                    title=title,
                    description=description,
                    active=active,
                    type=type,
                    order=order,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
                db_conn.session.add(new_field)
                db_conn.session.commit()

                return Fields(
                    id=uuid.uuid4(),
                    owner_id=owner_id,
                    title=title,
                    description=description,
                    active=active,
                    type=type,
                    order=order,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            except Exception as e:
                db_conn.session.rollback()
                raise e
            finally:
                db_conn.session.close()
