from flask import Flask
app = Flask(__name__)

@app.route("/clova/webhook")
def hello():
    print("/clova/webhook start")
    return "Hello World!!"

@app.route("/bot/webhook")
def hello():
    print("/bot/webhook start")
    return "Hello World!!"

if __name__ == "__main__":
    app.run()