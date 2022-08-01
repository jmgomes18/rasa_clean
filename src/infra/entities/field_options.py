from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from infra.config import Base
from infra.entities.fields import Fields
from datetime import datetime
import uuid


class FieldOptions(Base):
    __tablename__ = "field_options"
    __table_args__ = {"schema": "rasa"}
    __resource_name__ = {"singular": "field_option", "plural": "field_options"}

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    value = Column(String(50), nullable=False)
    field_id = Column(UUID(as_uuid=True), ForeignKey(Fields.id))
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self) -> str:
        return f"Form: [name={self.name}, value={self.value}, field_id{self.field_id}]"

    def __eq__(self, __other: object) -> bool:
        if (
            self.value == __other.value
            and self.name == __other.name
            and self.field_id == __other.field_id
        ):
            return True
        return False
