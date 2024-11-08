from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_posts = None
@app.route('/')
def home():
    global blog_posts
    blogposts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blogposts_url)
    if response.status_code == 200:
        blog_posts = response.json()

    return render_template("index.html", blog_posts=blog_posts)

@app.route("/blog/<int:id>")
def get_blog(id):
    if blog_posts:
        blog = next((post for post in blog_posts if post["id"] == id), None)
        if blog:
            return render_template("post.html", blog=blog)
        else:
            return "error while finding the specific blog post"
    else:
        return "No blog post is available"


if __name__ == "__main__":
    app.run(debug=True)
