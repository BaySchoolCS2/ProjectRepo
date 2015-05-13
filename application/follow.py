from application import app, collections
from collections import User, Subscriptions
from flask import session, redirect, url_for, abort

@app.route('/follow/<fuser>') #Defines URL for following users
def follow(fuser=None):
    if not session.get('logged_in'):
        return redirect(url_for('login')) #If the user is not logged in, redirect them to the login page
    try:
        user = User.objects(alias = session.get("alias")).get()
        fuser = User.objects(alias = fuser).get()
    except IndexError:
        abort(404) #If there is an error, return a 404 code s
    return Subscriptions.objects.get_or_create(user=user)
    # if fuser not in following.subscriptions:
    #     following.subscriptions.append(fuser)
    #     following.save()

    return redirect(url_for('profile', name = fuser.alias))
