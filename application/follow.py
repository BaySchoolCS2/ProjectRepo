from application import app, collections
from collections import User, Subscriptions
from flask import session, redirect, url_for, abort

@app.route('/follow/<fuser>') #Defines URL for following users
def follow(fuser=None):
    if not session.get('logged_in'):
        return redirect(url_for('login')) #If the user is not logged in, redirect them to the login page
    try:
        user = User.objects(alias = session.get("alias"))[0]
        fuser = User.objects(alias = fuser)[0]
    except IndexError:
        abort(404) #If there is an error, return a 404 code
    sub = Subscriptions.objects.get_or_create(user=user)[0]
    print(sub.subscriptions)
    if user not in sub.subscriptions:
        sub.subscriptions.append(user)
        print(sub.subscriptions[0].alias)
        sub.save()
    else:
        print('FAIL!')
    return redirect(url_for('profile', name = fuser.alias))

@app.route('/uFollow/<fuser>') #Defines URL for following users
def uFollow(fuser=None):
    if not session.get('logged_in'):
        return redirect(url_for('login')) #If the user is not logged in, redirect them to the login page
    try:
        user = User.objects(alias = session.get("alias")).get()
        fuser = User.objects(alias = fuser).get()
    except IndexError:
        abort(404) #If there is an error, return a 404 code s
    sub = Subscriptions.objects.get_or_create(user=user)[0]
    if user in sub.subscriptions:
        sub.subscriptions.remove(user)
        print(sub.subscriptions)
        sub.save()

    return redirect(url_for('profile', name = fuser.alias))
