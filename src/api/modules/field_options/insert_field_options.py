import logging
from api.adapter.adapter import adapter
from api.composer.register_field_options_composite import (
    register_field_options_composer,
)

logger = logging.getLogger(__name__)


def handler(event, context):
    try:
        print(event)
        response = adapter(request=event, api_route=register_field_options_composer())

        if response.status_code < 300:
            message = {
                "name": response.body.name,
                "value": response.body.value,
            }
            return {"statusCode": 201, "body": str(message)}
    except Exception as e:
        # Handling Errors
        logger.debug("crashed because: ", e)
        return {
            "statusCode": 500,
        }
