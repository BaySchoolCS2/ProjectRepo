from application import app, collections
from flask import render_template

@app.route('/')
def index():
	posts = []
	for post in collections.Posts.objects:
		posts.append(post)

	return render_template('index.html', posts = posts) # variables go after template

@app.route('/u')
@app.route('/u/<name>')
def profile(name = None, posts = ''):
    try:
        posts = collections.Posts.objects(author=collections.User.objects(alias=name)[0])  # returns a list of posts by alias
    except IndexError:
        pass
    return render_template('user.html', name = name, posts = posts)

@app.route('/p/')
@app.route('/p/<uid>')
def post(uid = None):
    try:
        content = collections.Posts.objects(id = uid)[0]
        err = 200
        print(content)
    except IndexError:
        err = 404
        post = None
    return render_template('post.html', post=content), err
