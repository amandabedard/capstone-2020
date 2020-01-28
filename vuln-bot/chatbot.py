import nltk
import numpy
import random
import string
from chat import Chat

GREETINGS_UTTERANCE = ("hello", "hi", "sup", "heyo", "hey")
GREETINGS_RESPONSE = ("hi", "hey", "hello", "howdy", "greetings")
ENDING_UTTERANCE = ("bye", "goodbye", "see ya", "later")

def init():
    chat = Chat()
    return chat

def greeting(chat):
    for word in chat.utterance.split():
        if word.lower() in GREETINGS_UTTERANCE:
            chat.text = random.choice(GREETINGS_RESPONSE)
        elif word.lower() in ENDING_UTTERANCE:
            if chat.auth == True:
                chat.end = True
                chat.text = "Goodbye, %s!" % chat.user
            else:
                chat.end = True
                chat.text = "Goodbye!"
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
            chat = greeting(chat)
            chat = authenticate(chat)

        return chat
    except:
        chat = init()
        chat.text = "Sorry, something went wrong. Please try again later"