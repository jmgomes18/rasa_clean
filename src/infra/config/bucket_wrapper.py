import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class BucketWrapper:
    def __init__(self, name):
        self.__client = self.__start_boto_client()
        self.buckets = self.list_buckets(self.__client)
        self.name = self.get_bucket_name(name)

    def get_boto_client(self):
        return self.__client

    def __start_boto_client(self):
        client = boto3.client("s3")
        return client

    def exists(self):
        """
        Determine whether the bucket exists and you have access to it.

        :return: True when the bucket exists; otherwise, False.
        """
        try:
            self.client.head_bucket(Bucket=self.bucket.name)
            logger.info("Bucket %s exists.", self.bucket.name)
            exists = True
        except ClientError:
            logger.warning(
                "Bucket %s doesn't exist or you don't have access to it.",
                self.bucket.name,
            )
            exists = False
        return exists

    @staticmethod
    def list_buckets(client):
        """
        Get the buckets in all Regions for the current account.

        :return: The list of buckets.
        """
        try:
            return client.list_buckets()
        except ClientError:
            logger.exception("Couldn't get buckets.")
            raise

    def get_bucket_name(self, name):
        try:
            bucket = []
            for bucket in self.buckets["Buckets"]:
                if bucket["Name"] == name:
                    bucket = bucket["Name"]
                    return bucket

            return None
        except ClientError:
            logging.warning(
                f"Bucket {name} doesn't exist or you don't have access to it."
            )

    def get_acl(self):
        """
        Get the ACL of the bucket.

        :return: The ACL of the bucket.
        """
        try:
            acl = self.bucket.Acl()
            logger.info(
                "Got ACL for bucket %s. Owner is %s.", self.bucket.name, acl.owner
            )
        except ClientError:
            logger.exception("Couldn't get ACL for bucket %s.", self.bucket.name)
            raise
        else:
            return acl

    def get_policy(self):
        """
        Get the security policy of the bucket.

        :return: The security policy of the specified bucket, in JSON format.
        """
        try:
            policy = self.bucket.Policy()
            logger.info(
                "Got policy %s for bucket '%s'.", policy.policy, self.bucket.name
            )
        except ClientError:
            logger.exception("Couldn't get policy for bucket '%s'.", self.bucket.name)
            raise
        else:
            return json.loads(policy.policy)

    def generate_presigned_post(self, object_key, expires_in):
        """
        Generate a presigned Amazon S3 POST request to upload a file.
        A presigned POST can be used for a limited time to let someone without an AWS
        account upload a file to a bucket.

        :param object_key: The object key to identify the uploaded object.
        :param expires_in: The number of seconds the presigned POST is valid.
        :return: A dictionary that contains the URL and form fields that contain
                 required access data.
        """
        try:
            response = self.bucket.meta.client.generate_presigned_post(
                Bucket=self.bucket.name, Key=object_key, ExpiresIn=expires_in
            )
            logger.info("Got presigned POST URL: %s", response["url"])
        except ClientError:
            logger.exception(
                "Couldn't get a presigned POST URL for bucket '%s' and object '%s'",
                self.bucket.name,
                object_key,
            )
            raise
        return response
