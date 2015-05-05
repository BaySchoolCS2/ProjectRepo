from application import app
from collections import User, Posts, Following
from flask import render_template, session, redirect, url_for
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

'''@app.route('/up/<user>')
def UVote(user=None):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    try:
        user = User.objects(alias = session.get("alias")).get()
        fuser = User.objects(alias = fuser).get()
    except IndexError:
        return 404
    sub = Following(user=user,following = [fuser])
    sub.save()
    return redirect(url_for('profile', name = fuser.alias'''
