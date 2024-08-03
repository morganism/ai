import boto3
import datetime
import os

REGION = os.environ.get('REGION')
INSTANCE_ID = os.environ.get('INSTANCE_ID')

def stop_instance_if_inactive(instance_id):
    region = REGION
    ec2 = boto3.client('ec2', region_name=region)
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    
    metrics = cloudwatch.get_metric_statistics(
        Period=300,
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(minutes=10),
        EndTime=datetime.datetime.utcnow(),
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Statistics=['Average'],
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}]
    )
    
    if metrics['Datapoints']:
        avg_cpu = metrics['Datapoints'][0]['Average']
        if avg_cpu < 10:  # Adjust threshold as needed
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Instance {instance_id} stopped due to inactivity")

if __name__ == "__main__":
    instance_id = INSTANCE_ID
    stop_instance_if_inactive(instance_id)


