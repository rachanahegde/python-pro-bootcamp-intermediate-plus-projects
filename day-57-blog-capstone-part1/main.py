from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    title = None
    subtitle = None
    body = None
    for post in all_posts:
        if post['id'] == index:
            title = post['title']
            subtitle = post['subtitle']
            body = post['body']
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
