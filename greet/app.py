from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "welcome"
@app.route("/welcome/home")
def welcome():
    return "welcome home"
@app.route_home("/welcome/back")
def welcome_back():
    return "welcome back"

