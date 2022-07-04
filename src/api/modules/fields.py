from src.domain.use_cases.fields.register_field import RegisterField
from src.data.repositories.fields.field_repository import FieldRepository


def handler(event, context):
    payload = event["body"]["field"]
    data = RegisterField(FieldRepository)
    data.registry(**payload)
    return {"message": "Success", "status_code": "201"}
