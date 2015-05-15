from application import app
from collections import User
from flask import session, render_template, flash, redirect, url_for
from forms import LoginForm
from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
        form is imported from froms.py
        session["logged_in"] is a boolean wether or not someone is logged in
        if you are already logged in you dont need to login, so you are redirected
        to index

        session['alias'] is the alias of the user that is currently logged in
        session['allowTracking'] is wether or not the user is to be tracked
        session['isMod'] is wether or not user is a moderator/advanced permission
        flash returns a string to be delayeds
    '''
    form = LoginForm()
    if session.get('logged_in'):
        return redirect(url_for('index'))
    if form.validate_on_submit():
        try:
            user = User.objects(email=form.email.data)[0]
            if check_password_hash(user.password, form.password.data):
                session['logged_in'] = True
                session['alias'] = user.alias
                session['allowTracking'] = user.allowTracking
                session['isMod'] = user.isMod
                session['isJudge'] = user.isJudge
                return redirect(url_for('index'))
            else:
                flash('Wrong password')
        except:
            flash('Wrong email, silly!')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    if session.get('logged_in'):
        session.pop('logged_in',None)
    return redirect(url_for('index'))
