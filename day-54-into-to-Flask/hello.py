from flask import Flask

#__name__ is a special attribute that tells us the name of the current class, function, method or descriptor  
app = Flask(__name__)

#functions are first-class objects, can be passed around as arguments 

#when the user hits up this route ("/")do hello_word
#@app.route is a python decorator -> function that gives additional functionality to an existent function
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

#Common way to use __name__
if __name__ == "__main__":
    app.run()