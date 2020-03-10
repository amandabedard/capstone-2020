class Chat:
    def __init__(self):
        self.end = False
        self.chatId = ''
        self.auth = False
        self.fullName = "Guest"
        self.accountNumber = 0
        self.text = ''
        self.lastRes = '#'
        self.lastUtt = '#'
        self.utterance = ''
        self.ipAddr = '0.0.0.0'

    def __str__(self):
        return str(self.__dict__)