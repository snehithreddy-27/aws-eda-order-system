import json

def handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        message = json.loads(body['Message'])
        print(f"📧 Sending email for order: {message['orderId']}")
        print(f"📦 Updating inventory for product: {message['productId']}")
    return {'statusCode': 200, 'body': 'Processed!'}
