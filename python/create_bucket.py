import boto3
import os

s3_client = boto3.client('s3')

response = s3_client.create_bucket(
    ACL='private',
    Bucket= os.getenv("S3_BUCKET_NAME"),
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'
    }
)

