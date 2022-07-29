import json
import logging
from api.services.create_presigned_url import CreatePresignedUrl


logger = logging.getLogger(__name__)


def handler(event, context):
    try:
        url = CreatePresignedUrl("field-service-bucket")
        url = url.create_presigned_post(object_name="file.png")

        return {
            "isBase64Encoded": True | False,
            "statusCode": 200,
            "body": {"url": url["url"]},
        }
    except (TypeError, RuntimeError) as e:
        logger.error(f"crashed here {e}")
        return {
            "headers": json.dumps(event["headers"]),
            "statusCode": 502,
            "body": {"message": "Something is broken"},
        }
