from src.domain.use_cases.fields.register_field import RegisterField
from src.infra.repositories.fields.field_repository import FieldRepository


def handler(event, context):
    print(type(event))
    payload = event["body"]
    data = RegisterField(FieldRepository)
    data.registry(**payload)
    return {"body": "Success", "statusCode": "201"}
