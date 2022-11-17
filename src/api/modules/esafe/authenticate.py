import logging
import os
import json

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

        return {
            "statusCode": 200,
            "body": json.dumps({"content": response["access_token"]}),
        }

    except RuntimeError as exc:
        logger.error("error", exc)
        return {
            "statusCode": 500,
            "body": {"message": "Something went wrong", "error": exc},
        }


def get_power_bi_token(event, context):
    params = event["queryStringParameters"]["access_token"]
    logger.info("auth token", params)

    handler = CreateMicrosoftAuth()

    response = handler.get_dashboard_data(params.replace('"', ""))

    return {"statusCode": 200, "body": json.dumps({"content": response})}
