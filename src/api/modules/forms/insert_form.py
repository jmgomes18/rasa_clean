import logging
from api.adapter.adapter import adapter
from api.composer.register_form_composite import register_form_composer

logger = logging.getLogger(__name__)


def handler(event, context):
    try:
        print(event["body"])
        response = adapter(request=event, api_route=register_form_composer())

        if response.status_code < 300:
            message = {
                "owner_id": response.body.owner_id,
                "title": response.body.title,
                "description": response.body.description,
                "active": response.body.active,
            }
            return {"statusCode": 201, "body": str(message)}
    except Exception as e:
        # Handling Errors
        logger.error(f"crashed here {e}")

        return {
            "statusCode": 500,
        }
