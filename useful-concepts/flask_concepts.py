from flask import Flask

app = Flask(__name__)
#If we want to get hold of what the user write in the url

#flask turns anything written after username/ as a variable and will store it as "name"
@app.route("/username/<name>")
def greet(name):
    return f"greeting {name}"