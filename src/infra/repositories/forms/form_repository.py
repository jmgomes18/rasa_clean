import uuid
from typing import List
from datetime import datetime
from infra.repositories.interfaces import Forms as Interface
from data.models.forms import Forms
from infra.config import DBConnectionHandler
from infra.entities import Forms as FormModel
from sqlalchemy.orm.exc import NoResultFound


class FormRepository(Interface):
    """Form Repository"""

    @classmethod
    def insert_form(
        cls,
        owner_id: uuid,
        title: str,
        description: str,
        active: bool,
    ) -> Forms:
        """
        Insert data in Forms entity
        :param - self
                - owner_id
                - title
                - description
                - active
                - created_at
                - updated_at
        :return - tuple with new form inserted
        """

        with DBConnectionHandler() as db:
            try:
                new_form = FormModel(
                    id=uuid.uuid4(),
                    owner_id=owner_id,
                    title=title,
                    description=description,
                    active=active,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
                db.session.add(new_form)
                db.session.commit()

                return Forms(
                    id=uuid.uuid4(),
                    owner_id=owner_id,
                    title=title,
                    description=description,
                    active=active,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()

    @classmethod
    def select(cls, form_id: str = None, active: bool = None) -> List[Forms]:
        with DBConnectionHandler() as db:
            try:
                if form_id and not active:
                    data = (
                        db.session.query(FormModel).filter(FormModel.id == id).first()
                    )
                elif active and not form_id:
                    data = (
                        db.session.query(FormModel)
                        .filter(FormModel.active == active)
                        .all()
                    )
                elif form_id and active:
                    data = db.session.query(FormModel).filter(
                        FormModel.id == form_id, FormModel.active == active
                    )
                else:
                    data = db.session.query(FormModel).all()

                return [data]
            except NoResultFound:
                return []
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()
