from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = MongoEngine(app)

app.jinja_env.globals["len"] = len


from application import login, home, signup
from application.api import api, ViewPosts, apiUrlWrap

api.add_resource(ViewPosts, apiUrlWrap('/posts/<string:user>'))
