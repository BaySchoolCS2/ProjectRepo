from application import app
from flask import render_template

@app.route('/about')
def about():
    return(render_template("about.html"))

@app.route('/rules')
def rules():
    return(render_template("rules.html"))

@app.route('/terms')
def terms():
    return(render_template("terms.html"))

@app.route('/help')
def help():
    return(render_template("help.html"))
