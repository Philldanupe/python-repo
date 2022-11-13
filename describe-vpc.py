import boto3

client=boto3.client("ec2")

# how to describe all vpc's available in acct

client.describe_vpcs()

x=client.describe_vpcs()

num_of_vpcs=x["Vpcs"]

for vpc in num_of_vpcs:
    print(vpc["VpcId"])
    
    
