from flask import Flask, render_template
from flask import render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    year_now = datetime.now().year
    return render_template("index.html", year=year_now)

@app.route("/guess/<name>")
def gender_age(name):
    response_age = requests.get(f"https://api.agify.io/?name={name}")
    response_gender = requests.get(f"https://api.genderize.io/?name={name}")
    gender = response_gender.json().get("gender")
    age = response_age.json().get("age")
    return render_template("guess.html", name=name, age=age, gender=gender)



if __name__ == "__main__":
    app.run(debug=True)

