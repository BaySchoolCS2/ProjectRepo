from application import app, collections
from flask import render_template, session, redirect, url_for,flash
from collections import User
from os import urandom
import hashlib
from forms import changePassword
from werkzeug.security import check_password_hash, generate_password_hash



@app.route('/settings', methods=['POST','GET'])
def settings():
    form = changePassword()


    if not session.get('logged_in'):

        return redirect(url_for('index'))
    user = User.objects(alias = session.get("alias")).get()

    if form.validate_on_submit():
        if check_password_hash(user.password, form.password.data):
            if form.newPassword.data == form.newPassword2.data and len(form.newPassword.data) >= 8:
                pw_hash = generate_password_hash(form.newPassword.data)
                user.password=pw_hash
                user.save()
                flash('Changed Password')
        else:
            flash('Wrong Password')

    return render_template('settings.html', apikey = user.apiKey, form = form)

@app.route('/generate_api_key')
def generateapikey():
    if not session.get("logged_in"):
        return redirect(url_for('index'))
    user = User.objects(alias = session.get("alias")).get()
    api_key = urandom(9).encode('base_64').replace("=","").strip()
    user.apiKey = api_key
    user.save()
    return redirect(url_for('settings'))
