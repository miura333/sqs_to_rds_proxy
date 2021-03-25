import json
import pymysql

def insert_rds(connection, id, data_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO analytics_data (id, data_id) VALUES (%s, %s)"
        r = cursor.execute(sql, (id, data_id))
        print(r) # -> 1
        connection.commit()

def lambda_handler(event, context):
    try:
        conn = pymysql.connect(user='USERNAME', passwd='PASSWORD', db='DB_NAME', host='RDS_PROXY_HOST')
    except Exception as e:
        print (e)

    print("SUCCESS: Connection to RDS mysql instance succeeded")

    for record in event['Records']:
        payload = json.loads(record["body"])
        print(payload)

        message_body = json.loads(payload['MessageBody'])
        print(message_body)

        insert_rds(conn, message_body['id'], message_body['data_id'])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
