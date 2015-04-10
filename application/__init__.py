from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_pyfile("config.cfg")
db = MongoEngine(app)

from application import login, home, signup
