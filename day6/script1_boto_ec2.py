#Goal is to create a scri[t to stopa ec2 machione based on instance.id


import boto3

instance_id = "12345"

def stops_ec2(ec2_id):
    
    try:
        ec2 = boto3.client("ec2")

        response = ec2.describe_instances(InstanceIds = [ec2_id])
        reservations = response.get("Reservations", [])
        if not reservations:
            print(f"No instances found with this if: {ec2_id}")
        else:
            print("-"*30)
            print(f"ec2 instance found with id: {ec2_id}, deleting now")
            ec2.stop_instances(InstanceIds=ec2_id)
            print(f"Instance stopped")

    except Exception as e:
        print(f"Unexpected Error happened: {e}")

stop_ec2(isntance_id)

