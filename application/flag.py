from application import app
from collections import Subscriptions, User, Posts
from flask import render_template, session, redirect, url_for, abort

@app.route("/flag/<type_>/<postid>")
def flag(type_=None, postid=None):
    if not session.get('logged_in'):
        abort(401)
    if type_  == None or postid == None:
        abort(404)
    return "derp"
