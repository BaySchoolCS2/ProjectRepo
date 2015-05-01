from application import app
from collections import Following, User
from flask import render_template, session, redirect, url_for

@app.route('/dashboard')
def dashboard():
    if session.get("logged_in"):
        user = User.objects(alias = session.get("alias"))
        Following.objects(user=user)
        return str(Following.following)
    else:
        return redirect(url_for("index"))
