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

    def __str__(self):
        return str(self.__dict__)