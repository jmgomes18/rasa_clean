import json
import logging
import os

from api.services.create_microsoft_auth import CreateMicrosoftAuth
from infra.config.bucket_wrapper import BucketWrapper

logger = logging.getLogger(__name__)


def get_microsoft_token(event, context):
    try:
        bucket = os.environ.get("BUCKET")

        handler = CreateMicrosoftAuth()
        s3 = BucketWrapper(bucket)

        if s3.credential_file_exists() and s3.check_object_creation_date():
            logger.info("Auth token still valid")
            return {"statusCode": 204}

        response = handler.login_power_bi()
        handler.store_credentials(bucket, response["access_token"])

        return {"statusCode": 200, "body": {"content": response}}
    except RuntimeError as exc:
        logger.error("error", exc)
        return {
            "statusCode": 500,
            "body": {"message": "Something went wrong", "error": exc},
        }


def get_power_bi_token(event, context):
    token = os.environ.get("TOKEN")
    handler = CreateMicrosoftAuth()
    response = handler.get_dashboard_data(token)
    return {"statusCode": 200, "body": {"content": json.loads(response.text)}}
