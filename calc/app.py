# Put your app in here.
from flask import Flask,request

from operations import add,sub,mult,div

app= Flask(__name__)

@app.route("/add")
def  calc_add():
    a= int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=add(a,b)
    return str(result)

@app.route("/sub")
def calc_sub():
    a= int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=sub(a,b)
    return str(result)

@app.route("/mult")
def calc_mult():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=mult(a,b)
    return str(result)

@app.route("/div")
def calc_div():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=div(a,b)
    return str(result)


operators ={
    "add":add,
    "sub":sub,
    "mult":mult,
    "div":div
    }

@app.route("/math/<operator>")
def calc_math(operator):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=operators[operator](a,b)
    return str(result)