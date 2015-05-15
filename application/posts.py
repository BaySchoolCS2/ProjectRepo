from application import app
from collections import User, Posts, Comment
from flask import session, render_template, redirect, flash, url_for, request
from forms import NewPost, NewComment
import uuid

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
        p = Posts(author = user, title = title, content = body, postid=str(uuid.uuid4())[:8])
        p.save()
        return redirect(url_for('viewPost', pid=str(p.postid)))
    return render_template("submitPost.html", form=form)

@app.route("/comment/<postid>", methods=["POST"])
def newComment(postid=None):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    if postid == None:
        abort(404)
    form = NewComment()
    if form.validate_on_submit():
        user = User.objects.get(alias=session.get("alias"))
        post = Posts.objects.get(postid=postid)
        c = Comment(author=user, body=form.content.data, commentid=str(uuid.uuid4())[:8])
        post.comments.append(c)
        post.save()
        return redirect(url_for("viewPost", pid=postid))
    else:
        return redirect(url_for("viewPost", pid=postid))
