from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello, world"

@app.route("/greet/<user_name>")
def greet(user_name):
    """
      INPUT: user_name for greeting
    """
    return f"hello, {user_name}"

@app.route("/index")
def index(): 
    return render_template('index.html', id=1121)

@app.route("/info")
def info(): 
    print(dir(request))
    print(request)
    print(request.cookies) 
    return "Info Captured"




