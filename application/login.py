from application import app
from collections import User
from flask import session, render_template, flash
from forms import LoginForm
from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(email=)
        if check_password_hash(User.password, form.password):
            session['logged_in'] = True
            session['alias'] = user.alias
            session['follow'] = user.allowTracking
            session['isMod'] = user.isMod
            return redirect(url_for('index'))
        else:
            flash("incorrect username or password")
        return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    return 'log out'
