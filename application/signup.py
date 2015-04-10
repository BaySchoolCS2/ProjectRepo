from application import app
from flask import session, render_template
from forms import SignupForm
from collections import User

@app.route("/signup")
def signup():
    form = SignupForm
    if session.get("logged_in"):
        return redirect(url_for("index"))
    if form.validate_on_submit():
        pass
        #what happens after the form is submitted
    return render_template("signup.html", form=form)
