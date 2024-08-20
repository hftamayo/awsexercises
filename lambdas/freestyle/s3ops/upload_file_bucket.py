import boto3

client = boto3.client('s3')

#upload a file to s3 bucket
client.upload_file('dailysales.txt', 's3automatebucket', 'dailysales.txt')

print("the sales file uploaded successfully")
