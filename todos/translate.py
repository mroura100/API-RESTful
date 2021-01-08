import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
tra = boto3.client('translate')


def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
   

    
    

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    
    traducir =  tra.translate_text(Text=result["Item"]["text"], SourceLanguageCode="auto", TargetLanguageCode=event['pathParameters']['lang'])
    result["Item"]["text"]=traducir

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
        
    }

    return response



