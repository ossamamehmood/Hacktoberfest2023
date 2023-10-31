import json
import boto3

# Set your SQS queue URL
SQS_QUEUE_URL = 'your-sqs-queue-url'

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sqs = boto3.client('sqs')
    
    for record in event['Records']:
        # Extract S3 bucket and object information from the event record
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Create a message to send to the SQS queue
        message = {
            'bucket': bucket,
            'key': key
        }
        
        # Send the message to the SQS queue
        response = sqs.send_message(
            QueueUrl=SQS_QUEUE_URL,
            MessageBody=json.dumps(message)
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('S3 data sent to SQS successfully!')
    }
