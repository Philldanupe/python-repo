import boto3

sess = boto3.Session(region_name='us-east-1')

s3client = sess.client('s3')

bucket_name = 'philldanupe-s3-boto3-training'

bucket_list = s3client.list_buckets()
#print(bucket_list['Buckets'])

for bucket in bucket_list['Buckets']:
    print(bucket['Name'])