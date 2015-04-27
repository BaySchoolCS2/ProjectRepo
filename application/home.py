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
    profile = User.objects.get_or_404()

    try:
        posts = collections.Posts.objects(author=profile.alias)
    except IndexError:
        pass
    return render_template('user.html', name = name, posts = posts)
