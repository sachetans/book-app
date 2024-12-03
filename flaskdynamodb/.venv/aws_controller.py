import boto3
from botocore.exceptions import ClientError

dynamo_client = boto3.client('dynamodb')

def get_items():
    return dynamo_client.scan(
        TableName='Books'
    )

def get_books(book_id, title, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    books_table = dynamodb.Table('Books')

    try:
        response = books_table.get_item(
            Key={'book_id': book_id, 'title': title})
    except ClientError as e:
            print(e.response['No item found'])
    else:
            return response['Item']
    
def add_book(books, jsonDat, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')

    books_table = dynamodb.Table('Books')
    response = books_table.put_item(
         Item = jsonDat
    )

    return response