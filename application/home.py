from application import app, collections
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html') # variables go after template

@app.route('/u/')
@app.route('/u/<name>')
def profile(name = None):
    posts = collections.Posts.objects(author=collections.User.objects(alias='bob')[0])
    return render_template('user.html', name = name, posts = posts)
