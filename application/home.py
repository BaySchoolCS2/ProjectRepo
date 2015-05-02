from application import app
from collections import User, Posts
from flask import render_template
from mongoengine import ValidationError, errors

@app.route('/')
def index():
	posts = []
	posts = Posts.objects.order_by('-score', '-created_at')

	return render_template('index.html', posts = posts) # variables go after template

@app.route('/u')
@app.route('/u/<name>')
def profile(name = None):
	posts = None
	profile = User.objects(alias = name).get_or_404()

	try:
		posts = Posts.objects(author = profile)
	except IndexError:
		pass
	return render_template('user.html', name = profile.alias, posts = posts)

@app.route('/p/')
@app.route('/p/<uid>')
def post(uid = None):
    try:
        content = Posts.objects(id = uid)[0]
        err = 200
        print(content)
    except ValidationError:
        err = 404
        content = ''
    return render_template('post.html', post=content), err
