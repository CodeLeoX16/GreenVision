import boto3
import os
from dotenv import load_dotenv
load_dotenv()

class S3Client:

    s3_client=None
    s3_resource = None
    def __init__(self, region_name=None):

        if S3Client.s3_resource==None or S3Client.s3_client==None:
            __access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
            __secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
            if __access_key_id is not None:
                __access_key_id = str(__access_key_id).strip().strip('"').strip("'")
            if __secret_access_key is not None:
                __secret_access_key = str(__secret_access_key).strip().strip('"').strip("'")
            if region_name is None:
                region_name = os.getenv("AWS_DEFAULT_REGION")
            if region_name is not None:
                region_name = str(region_name).strip().strip('"').strip("'")

            if __access_key_id is None:
                raise Exception("Environment variable: AWS_ACCESS_KEY_ID is not set.")
            if __secret_access_key is None:
                raise Exception("Environment variable: AWS_SECRET_ACCESS_KEY is not set.")
            if not region_name:
                raise Exception("Environment variable: AWS_DEFAULT_REGION is not set.")

            S3Client.s3_resource = boto3.resource('s3',
                                            aws_access_key_id=__access_key_id,
                                            aws_secret_access_key=__secret_access_key,
                                            region_name=region_name
                                            )
            S3Client.s3_client = boto3.client('s3',
                                        aws_access_key_id=__access_key_id,
                                        aws_secret_access_key=__secret_access_key,
                                        region_name=region_name
                                        )
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client

