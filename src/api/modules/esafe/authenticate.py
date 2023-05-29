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
            response = s3.get_file_content()
            logger.info("Auth token still valid")
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                },
                "body": json.dumps({"token": response}),
            }

        response = handler.login_power_bi()

        return {
            "statusCode": 200,
            "body": json.dumps({"content": response["access_token"]}),
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Acess-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            },
        }

    except RuntimeError as exc:
        logger.error("error", exc)
        return {
            "statusCode": 500,
            "body": {"message": "Something went wrong", "error": exc},
        }


def get_ups_token(event, context):
    try:
        bucket = os.environ.get("BUCKET")
        handler = CreateMicrosoftAuth()

        params = event["queryStringParameters"]["access_token"]
        logger.info("auth token", params)

        response = handler.get_ups_dashboard_data(params.replace('"', ""))

        handler.store_credentials(bucket, response)

        return {
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            },
            "statusCode": 200,
            "body": json.dumps({"content": response}),
        }
    except Exception as e:
        return {
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            },
            "statusCode": 502,
            "body": json.dumps({"error": e}),
        }
