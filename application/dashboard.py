from application import app
from collections import Following, User, Posts
from flask import render_template, session, redirect, url_for

@app.route('/dashboard')
def dashboard():
    if session.get("logged_in"):
        user = User.objects(alias = session.get("alias"))
        subscriptions = Following.objects(user=user).all()
        posts = []
        for subscription in subscriptions:
            p = Posts.objects(author=subscription).all()
            for post in p:
                posts.append(post)

        return render_template("dashboard.html", posts=posts)
    else:
        return redirect(url_for("index"))
