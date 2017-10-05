import boto3
from botocore.client import Config

## Defining AWS Key  , when accessing from remote server.

ACCESS_KEY_ID = 'AKIAJMXGZPEVMPdfdfdJOG25A'
ACCESS_SECRET_KEY = 'zT5b4WBmfDAktIdfdfdVInAKMQ2wf0DB3zEJfv+NTOxmu'
BUCKET_NAME = 'limton'
Region ='us-west-2'

ec2 = boto3.client('ec2','us-west-2',aws_access_key_id=ACCESS_KEY_ID,
      aws_secret_access_key=ACCESS_SECRET_KEY)

#Listing all the instance running in AWS
response = ec2.describe_instances()

#Fliter all the InstanceID from AWS

for Reservation in response['Reservations']:
    for Instance in Reservation['Instances']:
        print(Instance.get('InstanceId'))
