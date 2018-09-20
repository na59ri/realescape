from flask import Flask
app = Flask(__name__)

@app.route("/clova/webhook")
def hello():
    print("/clova/webhook start")
    return 'OK'

@app.route("/bot/webhook")
def hello():
    print("/bot/webhook start")
    return 'OK'

if __name__ == "__main__":
    app.run()