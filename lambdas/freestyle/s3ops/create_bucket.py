#import json module
import boto3

client = boto3.client('s3')

#create a s3 bucket
response = client.create_bucket(
    ACL='private',
    Bucket = 's3automatebucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    }
)

#return response
print("S3 bucket created successfully")
print(response)