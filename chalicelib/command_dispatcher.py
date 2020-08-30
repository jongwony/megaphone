import json
import pickle
import base64

import boto3


def main(chalice_req):
    # payload = {
    #     'payload': base64.b64encode(pickle.dumps(chalice_req.json_body))
    # }
    client = boto3.client('lambda')
    client.invoke(
        FunctionName='anon',
        InvocationType='Event',
        LogType='Tail',
        # Payload=json.dumps(payload),
        Payload=chalice_req.json_body,
    )


