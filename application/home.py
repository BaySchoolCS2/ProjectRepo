from application import app
from collections import User, Posts
from flask import render_template
from mongoengine import errors

@app.route('/')
@app.route('/<page>')
def index(page=1):
	page=int(page)
	if page == None:
		page = 1
	posts = Posts.objects.order_by('-sticky', '-score', '-created_at')
	paginated_posts = posts.paginate(page=page, per_page=5)
	return render_template('index.html', posts = paginated_posts, page = page) # variables go after template

@app.route('/u')
@app.route('/u/<name>')
def profile(name = None):
	
	posts = None
	profile = User.objects(alias = name).get_or_404()

	try:
		posts = Posts.objects(author = profile).order_by('-sticky', '-score', '-created_at')
	except IndexError:
		pass
	return render_template('user.html', name = profile.alias, posts = posts)
