import boto3

AWS_REGION = "us-east-1"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

for instances in ec2_resource.instances.all():
    print(f"ID: {instances.id}, State: {instances.state['Name']}")
