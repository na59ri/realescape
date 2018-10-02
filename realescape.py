import os
from flask import Flask, request

# 独自ライブラリ呼び出し
import sys
sys.path.append(os.getcwd() + '/control')
from lineBotController import LineBotController

app = Flask(__name__)


@app.route("/clova/webhook", methods=['POST'])
def hello_clova():
    print("/clova/webhook start")
    LineClovaController.action(request)
    return 'OK'


@app.route("/bot/webhook", methods=['POST'])
def receive_bot():
    print("/bot/webhook start")
    LineBotController.action(request)
    return 'OK'


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
