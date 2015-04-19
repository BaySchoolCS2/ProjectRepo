from application import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')#variables go after template

@app.route('/u/')
@app.route('/u/<name>')
def profile(name = None):
	return render_template('user.html', name = name)
