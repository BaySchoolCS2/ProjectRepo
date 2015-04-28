from application import app, collections
from flask import render_template
from mongoengine import ValidationError, errors

@app.route('/')
def index():
	posts = []
	for post in collections.Posts.objects:
		posts.append(post)

	return render_template('index.html', posts = posts) # variables go after template

@app.route('/u')
@app.route('/u/<name>')
def profile(name = None):
	posts = None
	profile = collections.User.objects(alias = name).get_or_404()

	try:
		posts = collections.Posts.objects(author = profile)
	except IndexError:
		pass
	return render_template('user.html', name = profile.alias, posts = posts)

@app.route('/p/')
@app.route('/p/<uid>')
def post(uid = None):
    try:
        content = collections.Posts.objects(id = uid)[0]
        err = 200
        print(content)
    except ValidationError:
        err = 404
        content = ''
    return render_template('post.html', post=content), err
