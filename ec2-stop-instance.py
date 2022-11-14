import boto3

ec2_client=boto3.client("ec2")

x=ec2_client.describe_instances()

data=x["Reservations"]

li=['i-01a301e0bdbe5b064', 'i-0516652d88ea2a160', 'i-017274b3f991f4ffa']

for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        

ec2_client.stop_instances(InstanceIds=li)
