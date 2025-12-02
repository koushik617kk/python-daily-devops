import boto3
import subprocess
from datetime import datetime

def get_date_bash():
    result = subprocess.run('date', capture_output=True, text=True, check=True)
    print(result)
    print(result.stdout)
    first_word = result.split()[0]
    # Check if the first word is 'Sat' or 'Sun'
    if first_word in ["Thu", "Sun"]:
        return True
    else:
        return False

def stop_ec2():
    ec2 = boto3.resource('ec2')
    
    running_instances = ec2.instances.filter( Filters=[{'Name' : 'instance-state-name', 'value': ['running']}])

    instance_id = [i.id for i in running_instances]

    if instance_id:
        ec2.instances.filter(InstanceIds=instance_ids).stop()
    else:
        print("NO instances are running")


if get_data_bash():
    stop_ec2()
else:
    print("Waiting for Thu and Sun")

