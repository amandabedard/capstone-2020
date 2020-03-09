import nltk
import numpy
import random
import string
from rivescript import RiveScript
from auth import checkAuth, accountBal
from chat import Chat

bot = RiveScript()
bot.load_directory("./rive")
bot.sort_replies()

def init(chatId=None):
    chat = Chat()
    return chat

def accountActions(chat):
    badAuthTxt= 'You must be authenticated to perform this action. Try authenticating with "authenticate".'

    if('withdraw' in chat.utterance.lower() or 'deposit' in chat.utterance.lower()):
        if (chat.auth == 'True' or chat.auth == True):
            chat.text = "If this were a real bot, the authenticated user would be able to perform these actions on the account"
        else:
            chat.text = badAuthTxt 
    elif('balance' in chat.utterance.lower()):
        if (chat.auth == 'True' or chat.auth == True):
            chat.text = 'This is the current value of your account: %s' % accountBal(chat)
        else:
            chat.text = badAuthTxt

def authenticate(chat):
    try:
        if not chat.auth and chat.lastRes == "Please give me your birthdate (MMDDYY) and the last 4 of your social, separated by a space to authenticate":
            # Call authentication function here
            print('Authenticating chat %s' % chat)
            chat = checkAuth(chat)
            if chat.auth:
                chat.text = "Authenticated! Thank you!"
            else:
                chat.text = "Failed to authenticate. Please try again."
        elif chat.lastRes == "Please give me your birthdate (MMDDYY) and the last 4 of your social, separated by a space to authenticate":
            chat.text = "Failed to authenticate. Please try again."
        elif chat.lastRes == "Ok, can I have an account number please?":
            chat.accountNumber = int(chat.utterance)
            chat.text = ''
        elif 'deauthenticate' in chat.utterance.lower() or 'logout' in chat.utterance.lower():
            chat.auth = False
            chat.accountNumber = 0
            chat.fullName = "Guest"
            chat.text = "You have been deauthenticated."
        else:
            print('Not Auth')
            chat.text = ''
    except:
        print('Auth error, skipping authentication')
        chat.text = 'Failed to authenticate. There was an internal error.'
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
            authenticate(chat)
            accountActions(chat)
            print(chat)
            if chat.text == '':
                chat.text = bot.reply(chat.chatId, chat.utterance.lower())
        return chat
    except:
        chat = init()
        chat.text = "Sorry, something went wrong. Please try again later"