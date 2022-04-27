import base64
import json
import boto3
import uuid
def write_to_sender(data):
    client = boto3.client('kinesis')
    
    response = client.put_record(
        StreamName='InboundStream',
        Data=data,
        PartitionKey=str(uuid.uuid4())
    )
    print(response)
    return response
    
def lambda_handler(event, context):
    print(event)
    data = json.loads(event.get('body'))
    print(data)
    if data.get('user_timespent') in [0, '0', None]:
        print("user_timespent missing or invalid")
        return
    payload=base64.b64encode(json.dumps(data).encode('utf-8'))
    print("Recieved data from kinesis")
    write_to_sender(payload)
    print("Object successfully sent to kinesis.")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')}  