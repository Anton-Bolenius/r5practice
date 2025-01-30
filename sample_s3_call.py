import boto3

ACCESS_KEY = ''
SECRET_KEY = ''


BUCKET_NAME = 'r5practice'

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)


s3_client = session.client('s3')

try:
    print(f"Listing objects in bucket: {BUCKET_NAME}")
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"- {obj['Key']} (Size: {obj['Size']} bytes, Last Modified: {obj['LastModified']})")
    else:
        print("The bucket is empty.")
except Exception as e:
    print(f"Error listing objects in bucket: {e}")