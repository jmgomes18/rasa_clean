from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from infra.config import Base
from datetime import datetime
import uuid


class Forms(Base):
    __tablename__ = "forms"
    __table_args__ = {"schema": "rasa"}
    __hidden_fields__ = {"owner_id"}
    __resource_name__ = {"singular": "form", "plural": "forms"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(String(100), nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )
    # Relationships
    form_fields = relationship("FormFields", back_populates="fields")

    def __repr__(self) -> str:
        return f"Form: [owner_id={self.owner_id}, title={self.title}, description={self.description}, active={self.active}]"

    def __eq__(self, __other: object) -> bool:
        if (
            self.owner_id == __other.owner_id
            and self.title == __other.title
            and self.description == __other.description
            and self.active == __other.active
        ):
            return True
        return False
