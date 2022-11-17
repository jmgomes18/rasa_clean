import os
import json
from requests import request
from datetime import datetime
from infra.config.bucket_wrapper import BucketWrapper


class CreateMicrosoftAuth:
    def __init__(self):
        self.grant_type = os.environ.get("GRANT_TYPE")
        self.secret = os.environ.get("SECRET_KEY")
        self.client_id = os.environ.get("CLIENT_ID")
        self.resource = os.environ.get("RESOURCE_ID")
        self.url = os.environ.get("LOGIN_URL")

    def login_power_bi(self):
        try:
            url = self.url
            payload = {
                "grant_type": self.grant_type,
                "client_secret": self.secret,
                "client_id": self.client_id,
                "resource": self.resource,
            }
            response = request("POST", url, data=payload)
            return json.loads(response.text)
        except RuntimeError:
            return {"statusCode": 500, "body": "Bad request"}

    def get_dashboard_data(self, token):
        group_id = os.environ.get("GROUP_ID")
        dashboard_id = os.environ.get("DASHBOARD_ID")
        dataset_id = os.environ.get("DATASET_ID")

        url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/dashboards/{dashboard_id}/GenerateToken"

        payload = json.dumps({"accessLevel": "View", "datasetId": dataset_id})
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

        response = request("POST", url, headers=headers, data=payload)

        return json.loads(response.text)

    def check_if_token_expired(self, expiration_date):
        check_date = datetime.strptime(expiration_date, "%Y-%m-%dT%H:%M:%SZ")

        if datetime.now() < check_date:
            return False

        return True

    def store_credentials(self, bucket, token):
        try:
            handler = BucketWrapper(bucket)

            handler.get_boto_client().put_object(
                Bucket=handler.name, Key="credentials.txt", Body=str.encode(token)
            )

        except RuntimeError as e:
            return {"error": json.dumps(e)}
