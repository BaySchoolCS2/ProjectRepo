from application import app
from collections import User, Posts, Following
from flask import render_template, session, redirect, url_for, flash
from mongoengine import ValidationError, errors

@app.route('/p/')
@app.route('/p/<uid>')
def post(uid = None):
    try:
        content = Posts.objects(id = uid)[0]
        err = 200
        print(content)
    except ValidationError:
        err = 404
        content = ''
    return render_template('post.html', post=content), err

@app.route('/follow/<fuser>')
def follow(fuser=None):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    try:
        user = User.objects(alias = session.get("alias")).get()
        fuser = User.objects(alias = fuser).get()
    except IndexError:
        return 404
    sub = Following(user=user,following = [fuser])
    sub.save()
    return redirect(url_for('profile', name = fuser.alias))

@app.route('/up/<post>')
def UVote(post=None):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    try:
        user = User.objects(alias = session.get("alias")).get()
        post = User.objects(id = post)
        if not(user in post.VotedUp.objects()):
            post.VotedUp = [user]
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
