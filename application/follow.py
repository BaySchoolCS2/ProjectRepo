from application import app, collections
from flask import session, redirect, url_for
from collections import User, Following

@app.route('/follow/<fuser>')
def follow(fuser=None):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    try:
        user = User.objects(alias = session.get("alias")).get()
        fuser = User.objects(alias = fuser).get()
        print(fuser.alias)
        print(user.alias)
    except IndexError:
        return 404
    sub = Following(user=user,following = [fuser])
    sub.save()
    return redirect(url_for('profile', name = fuser.alias))
