from flask import Flask
app = Flask(__name__)

@app.route("/clova/webhook")
def hello():
    return "Hello World!!"

@app.route("/bot/webhook")
def hello():
    return "Hello World!!"

if __name__ == "__main__":
    app.run()