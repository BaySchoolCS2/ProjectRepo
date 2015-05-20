from application import app
from collections import User
from forms import ForgotPassword
from flask import render_template, session, redirect, url_for

@app.route('/forgotpassword', methods=["POST","GET"])
def forgotpassword():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    form = ForgotPassword()

    if form.validate_on_submit():
        pass
    return render_template('ForgotPassword.html', form=form)
