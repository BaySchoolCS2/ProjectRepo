from application import app
from collections import User, Posts
from flask import render_template, session, redirect, url_for, flash
from mongoengine import ValidationError, errors

@app.route('/p/')
@app.route('/p/<pid>')
def viewPost(pid = None):
    up = False
    down = False
    if pid == None:
        return redirect(url_for('index'))
    try:
        content = Posts.objects(postid = pid)[0]
        err = 200
        print(content)
        if user in user.votedUp:
            up = True
    except IndexError:
        err = 404
        content = ''
    return render_template('post.html', post=content, up=up, down=down), err

@app.route('/up/<pid>')
def UVote(pid=None):
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = Posts.objects(postid = pid)[0]
        print(post.votedUp)
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
def unUpVote(pid=None):
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = Posts.objects(postid = pid)[0]
        print(post.votedUp)
        if user in post.votedUp:
            post.votedUp = [user]
            post.score -= 1
            post.save()
            return 'true'
        else:
            return 'false'
    except IndexError:
        return 404
