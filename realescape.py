from flask import Flask
app = Flask(__name__)


@app.route("/clova/webhook")
def hello():
    print("/clova/webhook start")
    return '200'


@app.route("/bot/webhook")
def hello():
    print("/bot/webhook start")
    return '200'


if __name__ == "__main__":
    app.run()
