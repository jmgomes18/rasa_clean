import logging
from infra.config.bucket_wrapper import BucketWrapper
from botocore.exceptions import ClientError


class CreatePresignedUrl:
    def __init__(self, name):
        self.name = name

    def create_presigned_post(
        self, object_name, fields=None, conditions=None, expiration=3600
    ):
        """Generate a presigned URL S3 POST request to upload a file

        :param bucket_name: string
        :param object_name: string
        :param fields: Dictionary of prefilled form fields
        :param conditions: List of conditions to include in the policy
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Dictionary with the following keys:
            url: URL to post to
            fields: Dictionary of form fields and values to submit with the POST
        :return: None if error.
        """

        config = BucketWrapper(self.name)
        client = config.get_boto_client()
        try:
            response = client.generate_presigned_post(
                config.name,
                object_name,
                Fields=fields,
                Conditions=conditions,
                ExpiresIn=expiration,
            )
        except ClientError as e:
            logging.error(e)
            return None

        return response
