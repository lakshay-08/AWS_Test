import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('customer_database')
s3 = boto3.resource('s3')
bucket_name = 'customers-bucket-572023'

def lambda_handler(event, context):
    phone_number = event['phone_number']
    phone_password = event['phone_password']
    
    # Update the DynamoDB record with the phone password
    response = table.get_item(Key={'phone_number': phone_number})
    if 'Item' in response:
        item = response['Item']
        item['phone_password'] = phone_password
        
        # Create a text file in the S3 bucket
        file_name = f'{phone_number}_password.txt'
        file_contents = f'Phone password: {phone_password}'
        bucket = s3.Bucket(bucket_name)
        object = bucket.put_object(Key=file_name, Body=file_contents)
        
        # Update the DynamoDB record with the file details
        item['file_name'] = file_name
        item['file_size'] = object.content_length
        item['file_timestamp'] = str(datetime.now())
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': 'Successfully updated DynamoDB and created file in S3'
        }
    else:
        return {
            'statusCode': 404,
            'body': 'Customer not found in DynamoDB'
        }
