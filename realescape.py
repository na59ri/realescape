import os
from flask import Flask, request
from .control import LineBotController

app = Flask(__name__)


@app.route("/clova/webhook", methods=['POST'])
def hello_clova():
    print("/clova/webhook start")
    return 'OK'


@app.route("/bot/webhook", methods=['POST'])
def receive_bot():
    print("/bot/webhook start")
    LineBotController.action(request)

    return 'OK'


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
