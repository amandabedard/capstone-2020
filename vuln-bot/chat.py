import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('capstoneChatSession')

class Chat:
    def __init__(self):
        self.end = False
        self.chatId = None
        self.auth = False
        self.fullName = "Guest"
        self.accountNumber = 0
        self.text = None
        self.lastRes = None
        self.lastUtt = None
        self.utterance = None
    def __str__(self):
        return str(self.__dict__)

    def checkSession(chatId):
        try:
            response = table.get_item(
                Key={
                    'chatId': chatId
                }
            )
            if response['Item']:
                item = json.dumps(response['Item'])
                self.end = item.end
                self.chatId = item.chatId
                self.auth = item.auth
                self.fullName = item.fullName
                self.accountNumber = item.accountNumber
                self.text = item.text
                self.lastRes = item.lastRes
                self.lastUtt = item.lastUtt
                self.utterance = item.utterance
            else:
                return self.__init__(self)
        except error:
            return self.__init__(self)
            
    def updateSession():
        try:
            table.update_item(
                Key={
                    'chatId': self.chatId,
                    'end': self.end,
                    'auth': self.auth,
                    'fullName': self.user,
                    'accountNumber': self.accountNumber,
                    'text': self.text,
                    'lastRes': self.lastRes,
                    'lastUtt': self.lastUtt,
                    'utterance': self.utterance
                }
            )
            return
        except error:
            print('Error updating, continuing with function')
            return