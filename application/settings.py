from application import app, collections
from flask import render_template

@app.route('/settings')
def settings():
    return render_template('settings.html')
