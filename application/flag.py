from application import app, mail
from collections import Subscriptions, User, Posts
from flask.ext.mail import Message
from flask import render_template, session, redirect, url_for, abort, flash

@app.route("/flag/<type_>/<postid>")
def flag(type_=None, postid=None):
    if not session.get('logged_in'):
        return redirect(url_for("index"))
    if type_  not in ["1","2","3","4"] or postid == None:
        abort(404)

    post = Posts.objects.get(postid=postid)
    if User.objects.get(alias=session.get("alias")) in post.flaggedBy:
        return redirect(url_for("index"))
    post.flaggedBy.append(User.objects.get(alias=session.get("alias")))
    post.flags += 1
    post.flagTypes.append(int(type_))
    post.save()

    mods = User.objects(isMod = True)
    mod_emails = []
    for mod in mods:
        mod_emails.append(mod.email)

    msg = Message("Post has been flagged",
        sender="whrlplcs@gmail.com",
        recipients=mod_emails)
    msg.body = "{0} has flagged a post by {1} entitled {2} for {3}".format(session.get("alias"), post.author.alias, post.title, type_)
    mail.send(msg)
    flash("You have flagged {0} by {1}".format(post.title, post.author.alias))
    return redirect(url_for("index"))

@app.route("/flagcomment/<type_>/<postid>")
def flagComment(type_=None, postid=None):
    if not session.get('logged_in'):
        abort(401)
    if type_  not in ["1","2","3","4"] or postid == None:
        abort(404)
