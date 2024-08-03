import boto3
import os

REGION = os.environ.get('REGION')
INSTANCE_ID = os.environ.get('INSTANCE_ID')

def start_instance(instance_id):
    region = REGION
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} started")

if __name__ == "__main__":
    instance_id = INSTANCE_ID
    start_instance(instance_id)

