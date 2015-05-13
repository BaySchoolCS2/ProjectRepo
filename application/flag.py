from application import app
from collections import Subscriptions, User, Posts
from flask import render_template, session, redirect, url_for, abort

@app.route("/flag/<type_>/<postid>")
def flag(type_=None, postid=None):
    if not session.get('logged_in'):
        abort(401)
    if type_  not in ["1","2","3","4"] or postid == None:
        abort(404)

    post = Posts.objects.get(postid=postid)
    post.flags += 1
    post.flagTypes.append(int(type_))
    post.save()
    return redirect(url_for("index"))

@app.route("/flagcomment/<type_>/<postid>")
def flagComment(type_=None, postid=None):
    if not session.get('logged_in'):
        abort(401)
    if type_  not in ["1","2","3","4"] or postid == None:
        abort(404)

    
