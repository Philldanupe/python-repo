import boto3

client=boto3.client("ec2")

client.delete_vpc(VpcId='vpc-0875420f415c6e6cf')
