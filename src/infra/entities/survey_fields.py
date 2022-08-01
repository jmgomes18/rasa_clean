from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from infra.config import Base
from infra.entities.surveys import Surveys
from infra.entities.fields import Fields
from datetime import datetime
import uuid


class SurveyFields(Base):
    __tablename__ = "survey_fields"
    __table_args__ = {"schema": "rasa"}
    __resource_name__ = {"singular": "survey", "plural": "surveys"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    value = Column(String(50), nullable=False)
    survey_id = Column(ForeignKey(Surveys.id), primary_key=True)
    field_id = Column(ForeignKey(Fields.id), primary_key=True)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )
    # Relationships
    fields = relationship("Fields")

    def __repr__(self) -> str:
        return f"Form: [name={self.value}, survey_id={self.survey_id}, field_id={self.field_id}]"

    def __eq__(self, __other: object) -> bool:
        if (
            self.field_id == __other.field_id
            and self.survey_id == __other.survey_id
            and self.name == __other.name
        ):
            return True
        return False
