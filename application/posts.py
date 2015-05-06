from application import app
from collections import User, Posts
from flask import session, render_template, redirect, flash, url_for, request

@app.route('/post', methods=["POST"])
def make_posts():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
#If the user tries to post and is not logged in, redirects them to login.

    body = request.form["data"]
    title = request.form["title"]
    user = User.objects(alias = session.get("alias")).get()
    p = Posts(author = user, title = title, content = body)
    p.save()
    print(p.id)
    return redirect(url_for('post', uid=str(p.id)))

@app.route('/CPost')
def posting_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('PostPage.html')
