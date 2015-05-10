from application import app
from collections import User, Posts
from forms import NewComment
from flask import render_template, session, redirect, url_for, flash
from mongoengine import ValidationError, errors

@app.route('/p/')
@app.route('/p/<pid>')
def viewPost(pid = None):
    newComment = NewComment()
    if pid == None:
        return redirect(url_for('index'))
    try:
        content = Posts.objects(postid = pid)[0]
        err = 200
        print(content)
    except IndexError:
        err = 404
        content = ''
    return render_template('post.html', post=content, comment=newComment), err

@app.route('/up/<pid>')
def UVote(pid=None):
    pid = pid.decode('ascii')
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = Posts.objects(postid = pid)[0]
        print(post.votedUp)
        if not(user in post.votedUp):
            post.votedUp = [user]
            post.score += 1
            post.save()
        else:
            flash("You already upvoted this post!")
            return redirect(url_for('veiwPost', pid = str(pid)))
    except IndexError:
        return 404
    return redirect(url_for('veiwPost', pid = pid))
