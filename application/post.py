from application import app
from collections import User, Posts, Comment
from forms import NewComment
from flask import render_template, session, redirect, url_for, flash
from mongoengine import ValidationError, errors
from forms import NewPost, NewComment
import uuid
import re

@app.route('/p/')
@app.route('/p/<pid>')
def viewPost(pid = None):
    newComment = NewComment()
    up = False
    down = False
    if pid == None:
        return redirect(url_for('index'))
    try:
        content = Posts.objects(postid = pid)[0]
        err = 200
    except IndexError:
        err = 404
        content = ''
    alias = session.get("alias")
    if alias != None:
        user = User.objects(alias = alias).get()
        if user in content.votedUp:
            up = True
        if user in content.votedDown:
            down = True
    return render_template('post.html', post=content, up=up, down=down, comment=newComment), err

@app.route('/up/<pid>')
def UVote(pid=None):
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = Posts.objects(postid = pid)[0]
        if not(user in post.votedUp):
            post.votedUp = [user]
            post.score += 1
            post.save()
            return 'true'
        else:
            return 'false'
    except IndexError:
        return 404

@app.route('/uUp/<pid>')
def uUVote(pid=None):
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = Posts.objects(postid = pid)[0]
        if user in post.votedUp:
            post.votedUp.remove(user)
            post.score -= 1
            post.save()
            return 'true'
        else:
            return 'false'
    except IndexError:
        return 404

@app.route('/dw/<pid>')
def DVote(pid=None):
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = Posts.objects(postid = pid)[0]
        if not(user in post.votedDown):
            post.votedDown = [user]
            post.score -= 1
            post.save()
            return 'true'
        else:
            return 'false'
    except IndexError:
        return 404

@app.route('/uDw/<pid>')
def uDVote(pid=None):
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = Posts.objects(postid = pid)[0]
        if user in post.votedDown:
            post.votedDown.remove(user)
            post.score += 1
            post.save()
            return 'true'
        else:
            return 'false'
    except IndexError:
        return 404

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
        content = form.content.data.split(" ")
        for c in content:
            if re.match('>{3}[0-9a-f]{8}\b', c) == None:
                c = Comment(author=user, body=content, commentid=str(uuid.uuid4())[:8])
                post.comments.append(c)
            post.save()
        return redirect(url_for("viewPost", pid=postid))
    else:
        return redirect(url_for("viewPost", pid=postid))
