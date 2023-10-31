import json
import boto3
import csv
import io

# Set your source DynamoDB table and destination S3 bucket information
DYNAMODB_TABLE_NAME = 'your-dynamodb-table-name'
S3_BUCKET_NAME = 'your-s3-bucket-name'
S3_OBJECT_KEY = 'exported-data.csv'  # S3 object key for the exported CSV file

def lambda_handler(event, context):
    # Initialize AWS clients for DynamoDB and S3
    dynamodb = boto3.resource('dynamodb')
    s3 = boto3.client('s3')

    # Get a reference to your DynamoDB table
    table = dynamodb.Table(DYNAMODB_TABLE_NAME)

    # Scan the DynamoDB table to fetch all records
    response = table.scan()

    # Extract and format the data from DynamoDB
    data = response.get('Items', [])

    # Prepare CSV data
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)

    # Write a header row (if needed) and the data rows
    csv_writer.writerow(data[0].keys()) if data else None
    for item in data:
        csv_writer.writerow(item.values())

    # Reset the buffer position
    csv_buffer.seek(0)

    # Upload the CSV data to the S3 bucket
    s3.upload_fileobj(csv_buffer, S3_BUCKET_NAME, S3_OBJECT_KEY)

    return {
        'statusCode': 200,
        'body': json.dumps('DynamoDB data exported to S3 successfully!')
    }
