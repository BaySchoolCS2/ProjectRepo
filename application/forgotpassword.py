from application import app
from collections import User
from forms import ForgotPassword
from flask import render_template, session, redirect, url_for
import uuid

@app.route('/forgotpassword/<code>', methods=["POST","GET"])
def forgotpassword(code = None):
    if session.get('logged_in'):
        return redirect(url_for('index'))
    form = ForgotPassword()
    if form.validate_on_submit():
        user = User.query() # get the user
        # set the code object via uuid4()
        msg = Message("Hello",
            sender="from@example.com",
            recipients=[form.email.data.lower()])
        msg.body = url_for("resetpassword", code=code)
        msg.html = "<a href='http://localhost:5000"+url_for("resetpassword", code=code)+"'>Reset Password</a>"
        mail.send(msg)
        # redirect to login
    return render_template('ForgotPassword.html', form=form)

@app.route('/resetpassword/<code>', methods=["POST","GET"])
def resetpassword(code=None):
    if code == None:
        return redirect(url_for('index'))

    # check if code is correct
    # reset password
    # redirect to login
