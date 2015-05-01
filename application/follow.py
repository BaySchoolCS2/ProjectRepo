from application import app, collections
from collections import User, Following
from flask import session, redirect, url_for

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
