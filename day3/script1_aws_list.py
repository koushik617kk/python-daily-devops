#write a script to list a few of your AWS respurces

import boto3

AWS_REGION= 'us-east-1'

ec2_client = boto3.client('ec2', region_name=AWS_REGION)

def list_ec2_instance():
    print(f"--listing EC2 instances in {AWS_REGION}")
    try:
        response = ec2_client.describe_instances()
        instance_count = 0

        for reservation in response['Reservation']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']

                instance_name = 'N/A'
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Name':
                        instance_name = tag['value']
                        break

                print(f"ID : {instance_id:<20} | Name: {instance_name:<20} | State: {instance_state:<10}")
                instance_count +=1

         print("-"*70)
         print(f"Total instnaces found: {instance_count}")
    
    except boto3.exceptions.NoCredentialsError:
        print("Error: AWS Credentials not found")

    except Exception as e:
        print(f"An unexpected Error occurfed: {e}")


list_ec2_instance()
