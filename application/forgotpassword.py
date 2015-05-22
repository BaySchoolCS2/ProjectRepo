from application import app
from collections import User
from forms import ForgotPassword
from flask import render_template, session, redirect, url_for
import uuid

@app.route('/forgotpassword/', methods=["POST","GET"])
def forgotpassword():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    form = ForgotPassword()
    if form.validate_on_submit():
        user = User.objects() # get the user
        # set the code object via uuid4()
        msg = Message("Hello")
            sender="from@example.com",
            recipients=[form.email.data.lower()])
        msg.body = url_for("resetpassword", code=str(uuid.uuid4()))
        msg.html = "<a href='http://localhost:5000"+url_for("resetpassword", code=code)+"'>Reset Password</a>"
        mail.send(msg)
        # redirect to login
    return render_template('ForgotPassword.html', form=form)

@app.route('/resetpassword/<code>', methods=["POST","GET"])
def resetpassword(code=None):
    if code == None:
        return redirect(url_for('index'))
    # check if code is correct
    form = ForgotPassword()
    if form.validate_on_submit():
        if form.password.data == form.password2.data and len(form.password.data) >= 8:
            pw_hash = generate_password_hash(form.password.data)
            try:
                user = User(password = pw_hash, color=str(uuid.uuid4())[:6])
                code = str(uuid.uuid4())
            except:
                pass

        else:
            if len(form.password.data) < 8:
                error = 'Password too short'
            else:
                error = 'Passwords do not match'
    # reset password
    return redirect(url_for('login'))
    # redirect to login
