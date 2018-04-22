import boto3

bucket_name = 'dominik.platos-bucket'

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

my_file = open('to_be_uploaded.txt','w+')
my_file.write('Here will be my test content, isnt it cool?')
my_file.close()

bucket.put_object(
  Key='omega/gamma/test.txt', 
  Body=open('to_be_uploaded.txt', 'rb')
)

