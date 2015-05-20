from application import app
from collections import User, Posts
from flask import redirect, url_for, abort, session, render_template

@app.route("/moderate")
def moderate():
    if not session.get("logged_in"):
        abort(404)
    if not session.get("isMod"):
        abort(404)
    user = User.objects.get(alias=session.get("alias"))
    posts = Posts.objects(flags__gte=1)
    p1 = []
    for post in posts:
        if user not in post.moderatedBy:
            p1.append(post)
    return render_template("mod_portal/flaggedPosts.html", posts=p1)

@app.route("/markasbad/<postid>")
def bad(postid=None):
    if not session.get("logged_in") or not session.get("isMod") or postid == None:
        abort(404)

    user = User.objects.get(alias=session.get("alias"))

    post = Posts.objects.get(postid=postid)
    if post.flags > 0:
        post.invisible = True
        post.moderated = True
        post.moderatedBy.append(user)
        post.save()
    return redirect(url_for("moderate"))

@app.route("/markasgood/<postid>")
def good(postid=None):
    if not session.get("logged_in") or not session.get("isMod") or postid == None:
        abort(404)
    user = User.objects.get(alias=session.get("alias"))

    post = Posts.objects.get(postid=postid)
    if post.flags > 0:
        post.moderated = True
        post.moderatedBy.append(user)
        post.save()
    return redirect(url_for("moderate"))
