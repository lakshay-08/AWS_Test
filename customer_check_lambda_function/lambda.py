import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('customer_database')

def lambda_handler(event, context):
    phone_number = event['phone_number']
    response = table.get_item(Key={'phone_number': phone_number})
    print(response['Item'])
    if 'Item' in response and response['Item'] is not None:
        has_password = False
        if 'phone_password' in response['Item']:
            has_password = True
        return {
            'customer_exists': True,
            'has_password': has_password
        }
    else:
        return {
            'customer_exists': False
        }
