import json
import boto3
import os

sns = boto3.client('sns')

def handler(event, context):
    order = {
        "orderId": "ORD-001",
        "amount": 99.99,
        "customerEmail": "customer@example.com",
        "productId": "PROD-123",
        "quantity": 2
    }
    sns.publish(
        TopicArn=os.environ['TOPIC_ARN'],
        Message=json.dumps(order),
        Subject='order.placed'
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Order placed successfully!')
    }
