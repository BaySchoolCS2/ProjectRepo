from application import app, collections
from flask import render_template, session, redirect, url_for



@app.route('/settings')

def settings():
    if not session.get('logged_in'):
        return redirect (url_for('index'))
    return render_template('settings.html')
