import boto3

ec2_client=boto3.client("ec2")

x=ec2_client.describe_instances()

data=x["Reservations"]

li=['i-0c2ec32ec87fec264','i-02c39f5d0089f9e82']

for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        

ec2_client.terminate_instances(InstanceIds=li)

