import base64
import json
import boto3
import uuid

def lambda_handler(event, context):
    for record in event['Records']:
        #Kinesis data is base64 encoded so decode here
        print(record)
        payload=base64.b64decode(record["kinesis"]["data"])
        print("Recieved data from kinesis")
        write_to_reciever(payload)
        print("Object successfully sent to kinesis.")
    
def write_to_reciever(data):
    client = boto3.client('kinesis')
    
    response = client.put_record(
        StreamName='OutboundStream',
        Data=data,
        PartitionKey=str(uuid.uuid4())
    )
    print(response)
    return response