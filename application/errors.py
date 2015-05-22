from application import app
from flask import render_template, session, redirect, url_for, send_from_directory
import os

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
# Enable once we have a 404 error page
@app.errorhandler(404)
def Error404(e):
    return render_template("errorpages/404.html"), 404
