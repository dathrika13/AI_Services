import json
import logging
import io
import os
import boto3
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
client = boto3.client('s3')
BASE_URL = os.getenv('APP_RUNNER_URL', 'https://ipfhhkpxvb.us-east-1.awsapprunner.com')

def lambda_handler(event, context):
    success = []
    fail = []
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        uri = f's3://{bucket}/{key}'
        collection = os.path.basename(os.path.dirname(uri))
        event_name = record['eventName']

        # Send request to App Runner service
        try:
            if event_name.startswith('ObjectCreated'):
                action = 'index'
                response = requests.post(f'{BASE_URL}/a/document?path={uri}&collection={collection}')
            elif event_name.startswith('ObjectRemoved'):
                action = 'remove'
                response = requests.delete(f'{BASE_URL}/a/document?path={uri}&collection={collection}')
            else:
                logger.error(f"Unsupported event type: {event_name}")
                fail.append(
                    {
                        'key': key,
                        'error': f'Unsupported event type: {event_name}'
                    })
                continue
            logger.info(f"Successfully triggered document processing for {key}")
            if str(response.status_code).startswith("20"):
                success.append(
                    {
                        'key': key,
                        'error': None
                    })
            else:
                fail.append(
                    {
                        'key': key,
                        'error': response.json()
                    })
        except requests.exceptions.RequestException as e:
            obj_resp = client.get_object(Bucket=bucket, Key=key)
            data = obj_resp['Body'].read().decode('utf-8')
            logger.error(f"Error triggering document processing for {key}: {str(e)}")
            fail.append(
                {
                    'key': key,
                    'error': str(e)
                })

    return {
        'statusCode': 200,
        'data': {
            'success': success,
            'fail': fail
        },
    }