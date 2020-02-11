import nltk
import numpy
import random
import string
from rivescript import RiveScript
from chat import Chat

bot = RiveScript()
bot.load_directory("./rive")
bot.sort_replies()

def init():
    chat = Chat()
    return chat

def authenticate(chat):
    if not chat.auth and chat.lastRes == "What is your SSN?":
        #TODO: Replace with actual authentication against a DB maybe?
        chat.auth = True
        chat.user.name = 'Amanda'
        chat.text = "Authenticated! Thank you!"
    elif chat.auth == False and chat.lastUtt == "authenticate":
        chat.text = "What is your SSN?"
    
    return chat


def chatWithBot(chat):
    try:
        if not chat:
            print("chatbot: No chat object, initializing")
            chat = init()
        else:
            print("chatbot: Chat object recieved. Processing.")

            chat.text = bot.reply('usr', chat.utterance.lower())

        return chat
    except:
        chat = init()
        chat.text = "Sorry, something went wrong. Please try again later"