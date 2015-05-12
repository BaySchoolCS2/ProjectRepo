from application import app
from collections import Subscriptions, User, Posts
from flask import render_template, session, redirect, url_for

@app.route('/dashboard')
def dashboard():
    if session.get("logged_in"):
        user = User.objects.get(alias = session.get("alias"))
        subscriptions=Subscriptions.objects.get_or_create(user=user)
        #posts = Posts.objects(author__in=subscriptions).order_by('-sticky', '-score', '-created_at')
        return str(subscriptions)
        #return render_template("dashboard.html", posts=posts)
    else:
        return redirect(url_for("index"))
