from application import app
from collections import User
from flask import session, render_template, flash, redirect, url_for
from forms import LoginForm
from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if session.get('logged_in'):
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User.objects(email=form.email.data)[0]
        if check_password_hash(user.password, form.password.data):
            session['logged_in'] = True
            session['alias'] = user.alias
            session['allowTracking'] = user.allowTracking
            session['isMod'] = user.isMod
            return redirect(url_for('index'))
        else:
            flash('incorrect username or password')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    return 'log out'
