from datetime import datetime
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.moment import Moment, _moment
from flask_wtf import CsrfProtect
from flask.ext.mail import Mail, Message

#Importing Flask and MongoEngine


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = MongoEngine(app)
moment = Moment(app)
CsrfProtect(app)
mail=Mail(app)


app.jinja_env.globals["len"] = len # allow len to be used in templates
app.jinja_env.globals["now"] = datetime.utcnow()
app.jinja_env.globals["str"] = str
app.jinja_env.globals["moment"] = _moment

#Importing all of the files for the project
from application import login
from application import home
from application import signup
from application import dashboard
from application import settings
from application import posts
from application import post
from application import judge
from application import follow
from application import flag
from application import moderators
from application import errors

from api import api, ViewPosts, apiUrlWrap, Me

api.add_resource(ViewPosts, apiUrlWrap('/posts/<string:user>'), apiUrlWrap('/posts'))
api.add_resource(Me, apiUrlWrap('/me'))
