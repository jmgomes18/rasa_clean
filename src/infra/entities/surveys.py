from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from infra.config import Base
from datetime import datetime
import uuid


class Surveys(Base):
    __tablename__ = "surveys"
    __table_args__ = {"schema": "rasa"}
    __hidden_fields__ = {"owner_id"}
    __resource_name__ = {"singular": "survey", "plural": "surveys"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    value = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    owner_id = Column(String(100), nullable=False)
    author_id = Column("author_id", UUID(as_uuid=True))
    time_elapsed = Column("time_elapsed", DateTime)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )
    # Relationships
    survey_fields = relationship("SurveyFields")

    def __repr__(self) -> str:
        return f"Form: [value={self.value}, status={self.status}, owner_id={self.owner_id}, author_id={self.author_id}, time_elapsed={self.time_elapsed}]"

    def __eq__(self, __other: object) -> bool:
        if (
            self.owner_id == __other.owner_id
            and self.author_id == __other.author_id
            and self.status == __other.status
            and self.time_elapsed == __other.time_elapsed
            and self.value == __other.value
            and self.status == __other.status
        ):
            return True
        return False
