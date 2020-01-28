import flask
from chatbot import init, chatWithBot
import sys

from flask import jsonify, request

app = flask.Flask(__name__)

def createChatDict(request, chat):
    chat.utterance = request.json.get("utterance")
    print("chatAPI: utterance is %s" % chat.utterance)
    return chat

@app.route('/chat', methods=["POST"])
def chat():

    try:
        print("chatAPI: starting API")
        chat = init()
        chat = createChatDict(request, chat)
        chat = chatWithBot(chat)

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