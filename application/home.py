from application import app
from collections import User, Posts, Subscriptions
from flask import render_template, session, abort
from mongoengine import errors

@app.route('/')
@app.route('/<page>') #Defines URL for home page
def index(page=1):
	try:
		page=int(page)
	except:
		abort(404)
	if page == None:
		page = 1

	posts = Posts.objects.order_by('-sticky', '-score', '-created_at') #Order for posts to be shown

	paginated_posts = posts.paginate(page=page, per_page=5)
	lenposts = len(posts)
	return render_template('index.html', posts = paginated_posts, page = page, lenposts = lenposts) # variables go after template

@app.route('/u') #Sets URL for user's pages
@app.route('/u/<name>')
def profile(name = None):
    posts = None
    try:
        user = User.objects(alias = session.get("alias"))[0]
    except IndexError:
        user = None
    profile = User.objects(alias = name).get_or_404() #Defines profile and gives a 404 if it can't be found
    follow = False
    try:
        sub = Subscriptions.objects.get_or_create(user=user)[0]
        if profile in sub.subscriptions:
            follow = True
    except IndexError:
        abort(500)
    try:
        posts = Posts.objects(author = profile).order_by('-sticky', '-score', '-created_at')
    except IndexError:
        pass
    return render_template('user.html', name = profile.alias, posts = posts, follow=follow) #Renders page based on the HTML file specified
