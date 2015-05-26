from application import app
from collections import User
from flask import render_template, session, redirect, url_for,flash
from forms import ChangePassword, ChangeColor
import hashlib
from os import urandom
from werkzeug.security import check_password_hash, generate_password_hash



@app.route('/settings', methods=['POST','GET'])
def settings():
    form = ChangePassword()
    changeColor = ChangeColor()


    if not session.get('logged_in'):
        return redirect(url_for('login'))
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
    elif changeColor.validate_on_submit():
        if len(changeColor.color.data) <= 6:
            for c in user.color:
                if c not in ["a","b","c","d","e","f","1","2","3","4","5","6","7","8","9","0"]:
                    return redirect(url_for('settings'))
            user.color = changeColor.color.data
            user.save()
    return render_template('settings.html', user = user, apikey = user.apiKey, form = form, changeColor = changeColor)

@app.route('/generate_api_key')
def generateapikey():
    if not session.get("logged_in"):
        return redirect(url_for('index'))
    user = User.objects(alias = session.get("alias")).get()
    api_key = urandom(9).encode('base_64').replace("=","").strip()
    user.apiKey = api_key
    user.save()
    return redirect(url_for('settings'))
