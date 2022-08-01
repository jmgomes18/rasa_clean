from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from infra.config import Base
from infra.entities.fields import Fields
from infra.entities.forms import Forms
from datetime import datetime
import uuid


class FormFields(Base):
    __tablename__ = "form_fields"
    __table_args__ = {"schema": "rasa"}
    __resource_name__ = {"singular": "form_field", "plural": "form_fields"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_id = Column(ForeignKey(Forms.id), primary_key=True)
    field_id = Column(ForeignKey(Fields.id), primary_key=True)
    section_id = Column(ForeignKey("section.id"))
    position = Column(Integer, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )
    # Relationships
    fields = relationship("Fields")

    def __repr__(self) -> str:
        return f"Form: [form_id={self.form_id}, field_id={self.field_id}, section_id={self.section_id}, position={self.position}]"

    def __eq__(self, __other: object) -> bool:
        if (
            self.form_id == __other.form_id
            and self.field_id == __other.field_id
            and self.section_id == __other.section_id
            and self.position == __other.position
        ):
            return True
        return False
