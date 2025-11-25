import boto3

instance_id = "1234"
region = "ap-south-1"


def start_instance(ec2_id, region)

    ec2 = boto3.resources(ec2_id, region_name=region)
    try:
        ec2_instance = ec2.Instance(ec2_id)

        currnt_status = ec2_instance.state['Name']

        if current_status == 'running':
            print(f"Instance is already in running state")
            retuen

        elif current_status == 'terminating' or current_status == 'shutting-down':
            print(f"Instance mis already there and are in termicating state")

        else:
            response = ec2_instance.start()

    
