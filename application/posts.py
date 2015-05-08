from application import app
from collections import User, Posts
from flask import session, render_template, redirect, flash, url_for, request
from forms import NewPost

@app.route('/post', methods=["POST", "GET"])
def makePosts():
    form = NewPost()
    if not session.get('logged_in'):
        return redirect(url_for('login'))
#If the user tries to post and is not logged in, redirects them to login.
    if form.validate_on_submit():
        body = form.body.data
        title = form.title.data
        user = User.objects(alias = session.get("alias")).get()
        p = Posts(author = user, title = title, content = body)
        p.save()
        return redirect(url_for('viewPost', pid=str(p.postid)))
    return render_template("submitPost.html", form=form)
