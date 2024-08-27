from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello there, World!</p>"

@app.route("/hello")
def hello():
    return "<p>Hello there, World!</p>"

@app.route("/goodbye")
def goodbye():
    return "<p>good bye!</p>"

