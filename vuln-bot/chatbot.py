import nltk
import numpy
import random
import string
from rivescript import RiveScript
from chat import Chat

bot = RiveScript()
bot.load_directory("./rive")
bot.sort_replies()

def init(chatId=None):
    chat = Chat()
    return chat

def authenticate(chat):
    if not chat.auth and chat.lastRes == "Please give me your birthdate (MMDDYY) and the last 4 of your social, separated by a space to authenticate":
        # Call authentication function here
        authenticated = True
        if authenticated:
            chat.auth = True
            chat.accountNumber = 12345
            chat.fullName = 'Amanda Bedard'
            chat.text = "Authenticated! Thank you!"
        else:
            chat.text = "Failed to authenticate. Please try again."
    elif chat.lastUtt == "Please give me your birthdate (MMDDYY) and the last 4 of your social, separated by a space to authenticate":
        chat.text = "Failed to authenticate. Please try again."
    
    return chat


def chatWithBot(chat):
    try:
        if not chat:
            print("chatbot: No chat object, initializing")
            chat = init()
        else:
            print("chatbot: Chat object recieved. Processing.")
            if chat.text != '':
                chat.lastRes = chat.text
            chat.text = bot.reply(chat.chatId, chat.utterance.lower())

        return chat
    except:
        chat = init()
        chat.text = "Sorry, something went wrong. Please try again later"