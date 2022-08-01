import uuid
from datetime import datetime
from infra.repositories.interfaces import FieldOptions as Interface
from data.models.field_options import FieldOptions
from infra.config import DBConnectionHandler
from infra.entities import FieldOptions as Model


class FieldOptionsRepository(Interface):
    """Field Repository"""

    @classmethod
    def insert_field_options(cls, name: str, value: str, field_id: str) -> FieldOptions:
        """
        Insert data in FieldOptions entity
        :param - self
                - name
                - value
                - field_id
        :return - tuple with new field options inserted
        """

        with DBConnectionHandler() as db:
            try:
                new_field = Model(
                    id=uuid.uuid4(),
                    name=name,
                    value=value,
                    field_id=field_id,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
                db.session.add(new_field)
                db.session.commit()

                return FieldOptions(
                    id=uuid.uuid4(),
                    name=name,
                    value=value,
                    field_id=field_id,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()
