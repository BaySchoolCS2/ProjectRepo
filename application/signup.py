from application import app
from collections import User
<<<<<<< HEAD
from flask import session, render_template, redirect, flash
=======
from mongoengine import ValidationError, errors
from flask import session, render_template, redirect, flash, url_for
>>>>>>> 052341e8a75119f7129260ff60e92397019ab30b
from forms import SignupForm
from werkzeug.security import generate_password_hash

@app.route('/signup', methods=['POST','GET'])
def signup():
    form = SignupForm()
    if session.get('logged_in'):
        return redirect(url_for('index'))
    if form.validate_on_submit():
        if form.password.data == form.password2.data and len(form.password.data) >= 8:
            pw_hash = generate_password_hash(form.password.data)
<<<<<<< HEAD
            user = User(email = form.email.data, alias = form.alias.data, password = pw_hash)
            try:
                user.save()
                return redirect(url_for("login"))
            except Exception, e:
                print('exception %s' % str(e))
                if 'Invalid Mail-address' in str(e):
                    flash('Invalid email')
=======
            try:
                user = User(email = form.email.data, alias = form.alias.data, password = pw_hash)
                user.save()
                return redirect(url_for('login'))
            except ValidationError:
                flash('Email is not an email')
            except errors.NotUniqueError:
                flash('Email or username is already in use')
        else:
            if len(form.password.data) < 8:
                flash('Password too short')
            else:
                flash('Passwords do not match')

>>>>>>> 052341e8a75119f7129260ff60e92397019ab30b
    return render_template('signup.html', form = form)
