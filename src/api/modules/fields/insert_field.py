from api.adapter.adapter import adapter
from api.composer.register_field_composite import register_field_composer


def handler(event, context):
    try:
        response = adapter(request=event, api_route=register_field_composer())

        if response.status_code < 300:
            message = {
                "owner_id": response.body.owner_id,
                "title": response.body.title,
                "description": response.body.description,
                "active": response.body.active,
                "type": response.body.type,
                "order": response.body.order,
            }
            return {"statusCode": 201, "body": str(message)}
    except Exception as e:
        # Handling Errors
        print(e)
        return {
            "statusCode": 500,
        }
