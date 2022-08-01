from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from infra.config import Base
from datetime import datetime
import uuid


class Sections(Base):
    __tablename__ = "sections"
    __table_args__ = {"schema": "rasa"}
    __resource_name__ = {"singular": "section", "plural": "sections"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    parent_id = Column(ForeignKey(id), primary_key=True)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )
    # Relationships
    children = relationship("Sections")

    def __repr__(self) -> str:
        return f"Form: [name={self.name}, parent_id={self.parent_id}]"

    def __eq__(self, __other: object) -> bool:
        if self.parent_id == __other.parent_id and self.name == __other.name:
            return True
        return False
