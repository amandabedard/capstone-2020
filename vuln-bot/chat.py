class Chat:
    def __init__(self):
        self.end = False
        self.auth = False
        self.user = None
        self.text = None
        self.lastRes = None
        self.lastUtt = None
        self.utterance = None
    def __str__(self):
        return str(self.__dict__)