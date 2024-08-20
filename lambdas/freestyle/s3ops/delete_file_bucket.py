import boto3

client = boto3.client('s3')

client.delete_object(Bucket='s3automatebucket', Key='dailysales.txt')

print("The file was deleted successfully")
