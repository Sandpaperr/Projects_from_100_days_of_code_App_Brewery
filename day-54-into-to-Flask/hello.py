from flask import Flask

#decorator for makking bold the text returned by another function
def make_bold(function):
    def wrapped_function():
        text = function()
        return f"<b>{text}</b>"
    return wrapped_function

def make_emphasis(function):
    def wrapped_function():
        text = function()
        return f"<em>{text}</em>"
    return wrapped_function

def make_underline(function):
    def wrapped_function():
        text = function()
        return f"<u>{text}</u>"
    return wrapped_function


#__name__ is a special attribute that tells us the name of the current class, function, method or descriptor  
app = Flask(__name__)

#functions are first-class objects, can be passed around as arguments 

#when the user hits up this route ("/")do hello_word
#@app.route is a python decorator -> function that gives additional functionality to an existent function
@app.route("/")
@make_bold
@make_underline
@make_emphasis
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"greeting {name}"

@app.route("/ub")
def greet_html():
    return f"<h1 style='text-align: center'>greeting </h1><p>this is a paragraph</p>"


#path capture everything between username and /1/ll...
@app.route("/username/<path:path>/1/ll/<int:number>/alba")
def greet_path(path, number):
    return f"greeting {path} {number}"





#Common way to use __name__
if __name__ == "__main__":
    app.run(debug=True)