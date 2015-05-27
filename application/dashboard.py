from application import app
from collections import Subscriptions, User, Posts
from flask import render_template, session, redirect, url_for

@app.route('/dashboard') #Defines URL for the dashboard
def dashboard():
    if session.get("logged_in"):
        user = User.objects.get(alias = session.get("alias"))
        subscriptions=Subscriptions.objects.get_or_create(user=user)[0]
        posts = Posts.objects(author__in=subscriptions.subscriptions).order_by('-sticky', '-score', '-created_at')
        print subscriptions
        return render_template("dashboard.html", posts=posts)
    else:
        return redirect(url_for("index"))
