import json
import boto3
import random
import string

def get_random_str(num):
    # 英数字をすべて取得
    dat = string.digits + string.ascii_lowercase + string.ascii_uppercase

    # 英数字からランダムに取得
    return ''.join([random.choice(dat) for i in range(num)])

def test_send_message(sqs):
    random_str = get_random_str(16)

    message_body = {'id': 'id_' + random_str, 'data_id': random_str}
    msg = {
        'MessageBody' : json.dumps(message_body)
    }

    response = sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/xxxxxxxxxx/',
        DelaySeconds=0,
        MessageBody=(
            json.dumps(msg)
        )
    )
    print(response)

def lambda_handler(event, context):

    sqs = boto3.client('sqs')

    for i in range(100):
        test_send_message(sqs)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
