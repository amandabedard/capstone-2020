import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('capstoneAuthTable')

def checkAuth(chat):
    try:
        response = table.get_item(
                Key={
                    'accountNumber': int(chat.accountNumber)
                }
            )
        print(response)
        if 'Item' in response:
            item = response['Item']
            check = chat.utterance.split()
            print(check)
            if item['birthday'] == check[0] and item['lastFour'] == check[1]:
                chat.fullName = item['fullName']
                chat.auth = True
            else:
                chat.accountNumber = 0
    except:
        chat.accountNumber = 0
    
    return chat