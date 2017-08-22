from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/configservices/v1/stacknames")
def stacknames():
    return "Stack names will be displayed later\n"

@app.route("/configservices/v1/stackconfig")
def stacknames():
    return "Stack configs will be added later\n"
