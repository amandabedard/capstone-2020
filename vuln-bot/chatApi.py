import flask
from chatbot import init, chatWithBot
from chatSession import checkSession, updateSession
import sys
import uuid

from flask import jsonify, request

app = flask.Flask(__name__)

def createChatDict(request, chat):
    chat.utterance = request.json.get("utterance")
    # Checking to see if there's an ongoing chat session
    if request.json.get("chatId"):
        chat.checkSession(request.json.get("chatId"))
    else:
        chat.chatId = uuid.uuid4()
        
    print("chatAPI: utterance is %s" % chat.utterance)
    return chat

@app.route('/chat', methods=["POST"])
def chat():

    try:
        print("chatAPI: starting API")
        chat = init()
        chat = createChatDict(request, chat)
        chat = chatWithBot(chat)
        chat.updateSession()

        res = {
            "status": 200,
            "response": chat.text,
            "metadata": str(chat)
        }
        return jsonify(res)

    except:
        res = {
            "status": 500,
            "error": "API Error: %s" % sys.exc_info()[0]
        }
        return jsonify(res)


app.run()