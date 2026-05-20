import json

def handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        message = json.loads(body['Message'])
        print(f"💳 Processing payment for order: {message['orderId']}")
        print(f"💰 Amount: ${message['amount']}")
    return {'statusCode': 200, 'body': 'Payment processed!'}
