import boto3
import os

def connect_to_s3():
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('S3_ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('S3_SECRET_KEY_ID')
    )
    return s3