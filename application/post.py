from application import app
from collections import User, Posts
from flask import render_template, session, redirect, url_for, flash
from mongoengine import ValidationError, errors

@app.route('/p/')
@app.route('/p/<pid>')
def viewPost(pid = None):
    if pid == None:
        return redirect(url_for('index'))
    try:
        content = Posts.objects(postid = pid)[0]
        err = 200
        print(content)
    except IndexError:
        err = 404
        content = ''
    return render_template('post.html', post=content), err

@app.route('/up/<post>')
def UVote(post=None):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = User.objects(id = post)
        if not(user in post.votedUp.objects()):
            post.votedUp = [user]
            post.score += 1
            post.save()
        else:
            flash("You already upvoted this post!")
            return redirect(url_for('profile', name = fuser.alias))
    except IndexError:
        return 404
    sub = Posts.objects(user=user,following = [fuser])
    sub.save()
    return redirect(url_for('profile', name = fuser.alias))
