import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('capstoneChatSession')

def checkSession(chat, chatId):
    try:
        response = table.get_item(
            Key={
                'chatId': chatId
            }
        )
        if 'Item' in response:
            item = response['Item']
            chat.end = item['endChat']
            chat.chatId = item['chatId']
            chat.auth = item['authorized']
            chat.fullName = item['fullName']
            chat.accountNumber = item['accountNumber']
            chat.text = item['chatText']
            chat.lastRes = item['lastRes']
            chat.lastUtt = item['lastUtt']
            chat.utterance = item['utterance']
            chat.ipAddr = item['ipAddr']
            chat.exists = True
        else:
            chat.exists = False
            return chat
    except error:
        chat.exists = False
        return chat
            
def updateSession(chat):
        try:
            tableKey = {
                    'chatId': chat.chatId
            }
            attributes = {
                    ':endChat': chat.end,
                    ':authorized': chat.auth,
                    ':fullName': chat.fullName,
                    ':accountNumber': chat.accountNumber,
                    ':chatText': chat.text,
                    ':lastRes': chat.lastRes,
                    ':lastUtt': chat.lastUtt,
                    ':utterance': chat.utterance,
                    ':ipAddr': chat.ipAddr
            }
            table.update_item(
                Key=tableKey,
                UpdateExpression="SET ipAddr= :ipAddr, endChat= :endChat, authorized= :authorized, fullName= :fullName, accountNumber= :accountNumber, chatText= :chatText, lastRes= :lastRes, lastUtt= :lastUtt, utterance= :utterance",
                ExpressionAttributeValues=attributes
            )
            return
        except:
            print('Error updating, continuing with function')
            return