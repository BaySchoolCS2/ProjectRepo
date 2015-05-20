from application import app
from collections import User
from flask import session, render_template, flash, redirect, url_for

@app.route("/verifyemail/<code>")
def verifyemail(code=None):
    try:
        u = User.objects.get(emailVerifyKey=code)
    except IndexError:
        abort(404)

    u.emailVerified = True
    u.save()

    flash("Your email has been verified")
    return redirect(url_for("login"))
