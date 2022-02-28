import json
from flask import Flask, render_template, request
from utils import load_data, get_post, load_comments, get_comment, search_post, search_user_post

app = Flask(__name__)


@app.route('/')
def index():
    posts = load_data()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:uid>')
def view_post(uid):
    comments = get_comment(uid)
    post = get_post(uid)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search', methods=["GET", "POST"])
def search():
    name = request.form.get('name')
    posts = search_post(name)
    return render_template('search.html', posts=posts, req=name)


@app.route('/users/<string:username>')
def post_user(username):
    posts = search_user_post(username)
    return render_template('user-feed.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
