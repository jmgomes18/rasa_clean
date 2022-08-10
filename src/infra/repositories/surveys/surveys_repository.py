import uuid
from typing import List
from datetime import datetime
from infra.repositories.interfaces import Surveys as Interface
from data.models.surveys import Surveys
from infra.config import DBConnectionHandler
from infra.entities import Surveys as SurveyModel
from sqlalchemy.orm.exc import NoResultFound


class SurveysRepository(Interface):
    """Field Repository"""

    @classmethod
    def insert_survey(
        cls, owner_id: uuid, value: str, status: str, author_id: uuid, time_elapsed
    ) -> Surveys:
        """
        Insert data in Surveys entity
        :param - self
                - owner_id
                - value
                - status
                - author_id
                - time_elapsed
                - created_at
                - updated_at
        :return - tuple with new survey inserted
        """

        with DBConnectionHandler() as db:
            try:
                new_survey = SurveyModel(
                    id=uuid.uuid4(),
                    owner_id=owner_id,
                    value=value,
                    status=status,
                    author_id=author_id,
                    time_elapsed=time_elapsed,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
                db.session.add(new_survey)
                db.session.commit()

                return Surveys(
                    id=uuid.uuid4(),
                    owner_id=owner_id,
                    value=value,
                    status=status,
                    author_id=author_id,
                    time_elapsed=time_elapsed,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()

    @classmethod
    def select(cls, survey_id: str = None, status: str = None) -> List[Surveys]:
        with DBConnectionHandler() as db:
            try:
                if survey_id and not status:
                    data = (
                        db.session.query(SurveyModel)
                        .filter(SurveyModel.id == survey_id)
                        .all()
                    )
                elif status and not survey_id:
                    data = (
                        db.session.query(SurveyModel)
                        .filter(SurveyModel.status == status)
                        .all()
                    )
                elif survey_id and status:
                    data = db.session.query(SurveyModel).filter(
                        SurveyModel.id == survey_id, SurveyModel.status == status
                    )
                else:
                    data = db.session.query(SurveyModel).all()

                return [data]
            except NoResultFound:
                return []
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()
