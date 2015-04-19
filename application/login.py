from application import app
from flask import session, render_template
from forms import LoginForm
from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
        #what happens after form is submitted goes here
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    return 'log out'
