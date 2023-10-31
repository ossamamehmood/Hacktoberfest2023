import json
import boto3

# Set your DynamoDB table name
DYNAMODB_TABLE_NAME = 'your-dynamodb-table-name'

# Initialize AWS DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

def lambda_handler(event, context):
    try:
        # Parse the request body from the API Gateway event
        request_body = json.loads(event['body'])

        # Define the item to be stored in DynamoDB
        dynamodb_item = {
            'PrimaryKey': request_body['primary_key'],  # Change 'PrimaryKey' to your actual primary key attribute name
            'OtherAttribute1': request_body['other_attribute_1'],
            'OtherAttribute2': request_body['other_attribute_2'],
            # Add more attributes as needed
        }

        # Put the item into the DynamoDB table
        response = table.put_item(Item=dynamodb_item)

        return {
            'statusCode': 200,
            'body': json.dumps('Data stored in DynamoDB successfully!')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error: ' + str(e))
        }
