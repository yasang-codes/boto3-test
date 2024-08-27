import json
import boto3
from os import environ
from botocore.exceptions import ClientError

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table_name = environ.get('USERS_TABLE')
    if not table_name:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "USERS_TABLE environment variable not set"})
        }

    table = dynamodb.Table(table_name)
    
    try:
        table_response = table.scan()
        response = {"statusCode": 200, "body": json.dumps(table_response)}
    except ClientError as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    return response