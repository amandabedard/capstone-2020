import flask
from chatbot import init, chatWithBot
from chatSession import checkSession, updateSession
import sys
import uuid
import json

from flask import jsonify, request

app = flask.Flask(__name__)

def createChatDict(request, chat):
    # Checking to see if there's an ongoing chat session
    if "chatId" in request.json:
        checkSession(chat, request.json.get("chatId"))
    else:
        chat.chatId = str(uuid.uuid1())
    
    if chat.utterance != '':
        chat.lastUtt = chat.utterance
        chat.utterance = ''
    chat.utterance = request.json.get("utterance")
        
    print("chatAPI: utterance is %s" % chat.utterance)
    return chat

@app.route('/chat', methods=["POST"])
def chat():

    # try:
        print("chatAPI: starting API")
        chat = init()
        chat = createChatDict(request, chat)
        chat = chatWithBot(chat)

        print(chat)
        updateSession(chat)

        res = {
            "status": 200,
            "response": chat.text,
            "metadata": str(chat)
        }
        return jsonify(res)

    # except:
        res = {
            "status": 500,
            "error": "API Error: %s" % sys.exc_info()[0]
        }
        return jsonify(res)


app.run()