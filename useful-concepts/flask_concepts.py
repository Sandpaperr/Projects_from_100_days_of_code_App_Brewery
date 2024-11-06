from flask import Flask

app = Flask(__name__)
#If we want to get hold of what the user write in the url

#flask turns anything written where <name> is as a variable and will store it as "name"
@app.route("/username/<name>")
def greet(name):
    return f"greeting {name}"

# we can also store the path from <name> to everything after that
#path capture everything between username and /1/ll...
@app.route("/username/<path:path>/1/ll/<int:number>/alba")
def greet(path, number):
    return f"greeting {path}"


# app.route decorator allow the return to be html
@app.route("/ub")
def greet():
    return f"<h1>greeting </h1>"

# DEBUG MODE -> allows to activate the debugger and automatic reload 

#__name__ is a special attribute that tells us the name of the current class, function, method or descriptor  
#if name == main allow us to run from the code instead of the console "flusk run"
if __name__ == "__main__":
    app.run(debug=True)