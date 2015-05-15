from application import app
from collections import User
from flask import session, render_template, redirect, flash, url_for, request
from forms import SignupForm
from mongoengine import ValidationError, errors
import uuid
from werkzeug.security import generate_password_hash

@app.route('/signup', methods=['POST','GET'])
def signup():
    """
        Signup, creates a new user
        if the session is logged in return to index
        when form is valided if the passwords match and the password length is
        greater than 8 characters then create the password hash
        if it is not the throw errors

        try to create the user object and catch all expected errors.
    """
    form = SignupForm()

    error = None

    if session.get('logged_in'):
        return redirect(url_for('index'))

    if form.validate_on_submit():
        if form.password.data == form.password2.data and len(form.password.data) >= 8:
            pw_hash = generate_password_hash(form.password.data)
            try:
                user = User(email = form.email.data.lower(), alias = form.alias.data, password = pw_hash, color=str(uuid.uuid4())[:6])
                if len(User.objects) == 0:
                    user.isMod = True
                    user.isJudge = True
                user.save()
                return redirect(url_for('login'))
            except ValidationError:
                error = 'Email is not an email'
            except errors.NotUniqueError:
                error = 'Email or username is already in use'
        else:
            if len(form.password.data) < 8:
                error = 'Password too short'
            else:
                error = 'Passwords do not match'

    return render_template('signup.html', form = form, err = error)
