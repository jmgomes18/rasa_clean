import uuid
from typing import List
from datetime import datetime
from infra.repositories.interfaces import Fields as Interface
from data.models.fields import Fields
from infra.config import DBConnectionHandler
from infra.entities import Fields as FieldModel
from sqlalchemy.orm.exc import NoResultFound


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

        with DBConnectionHandler() as db:
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
                db.session.add(new_field)
                db.session.commit()

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
                db.session.rollback()
                raise e
            finally:
                db.session.close()

    @classmethod
    def select(cls, field_id: str = None, active: bool = None) -> List[Fields]:
        with DBConnectionHandler() as db:
            try:
                if field_id and not active:
                    data = (
                        db.session.query(FieldModel)
                        .filter(FieldModel.id == field_id)
                        .all()
                    )
                elif active and not field_id:
                    data = (
                        db.session.query(FieldModel)
                        .filter(FieldModel.active == active)
                        .all()
                    )
                elif field_id and active:
                    data = db.session.query(FieldModel).filter(
                        FieldModel.id == field_id, FieldModel.active == active
                    )
                else:
                    data = db.session.query(FieldModel).all()

                return [data]
            except NoResultFound:
                return []
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()
