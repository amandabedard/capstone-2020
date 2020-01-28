import flask
import chatbot

from flask import jsonify

app = flask.Flask(__name__)

def createChatDict(request):
    chat.utterance = request.json.get("utterance")
    return chat

@app.route('/chat')
def chat():
    try:
        chat = chatbot.init()
        chat = createChatDict(request)
        chat = chatbot.chatWithBot(chat)

        res = {
            "status": 200,
            "body": chat
        }
        return jsonify(res)

    except Error as err:
        res = {
            "status": 500,
            "error": err
        }
        return jsonify(res)


app.run()