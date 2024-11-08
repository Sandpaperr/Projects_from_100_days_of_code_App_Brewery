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

@app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/f1cf8b82e5bff7a67843"
    response = requests.get("https://api.npoint.io/f1cf8b82e5bff7a67843")
    if response.status_code == 200:
        blog_post_dict = response.json()
        return render_template("blog.html", posts=blog_post_dict)



if __name__ == "__main__":
    app.run(debug=True)

