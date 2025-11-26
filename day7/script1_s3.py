import boto3

S3_Name = "abc"
Region = 'ap-south-1'

s3_client = boto3.client("s3")

def create_s3(s3_name, region, s3_client):
    try:
        if region == "us-east-1":
            response = s3_client.create_bucket(Bucket=s3_name)

        else:
            response = s3_client.create_bucket(Bucket=s3_name, CreateBucketConfiguration = {'LocationConstraint': region})

        print(f"Created s3 bucket:")


create_s3(S3_Name, Region, s3_client)


