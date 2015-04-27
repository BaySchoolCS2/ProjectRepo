from application import app, db
from flask import render_template, session, redirect, url_for
from collections import Following

@app.route('/dashboard')
def dashboard():
    if session.get("logged_in"):
        return render_template("dashboard.html")
    else:
        return redirect(url_for("index"))
