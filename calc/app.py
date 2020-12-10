from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route("/add")
def perform_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    return str(result)

@app.route("/sub")
def perform_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return str(result)

@app.route("/mult")
def perform_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return str(result)

@app.route("/div")
def perform_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return str(result)

@app.route("/math/<function>")
def perform_all(function):
    if function == "add":
        return str(add(int(request.args["a"]), int(request.args["b"])))
    elif function == "sub":
        return str(sub(int(request.args["a"]), int(request.args["b"])))
    elif function == "mult":
        return str(mult(int(request.args["a"]), int(request.args["b"])))
    elif function == "div":
        return str(div(int(request.args["a"]), int(request.args["b"])))
    else: 
        return "wrong direction"
