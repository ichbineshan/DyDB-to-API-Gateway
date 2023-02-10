import boto3
import json

# define the DynamoDB table that Lambda will connect to
tableName = "employee"

# create the DynamoDB resource
dynamo = boto3.resource('dynamodb').Table(tableName)

print('Loading function')

def lambda_handler(event, context):
    try:
        idval=event.get('id')
        queryData=dynamo.get_item(Key={'id':idval})
        return queryData['Item']
    except Exception as e:
        print(e)