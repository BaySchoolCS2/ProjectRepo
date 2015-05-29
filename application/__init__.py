from datetime import datetime
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.moment import Moment, _moment
from flask_wtf import CsrfProtect
from flask.ext.mail import Mail

#Importing Flask and MongoEngine

app = Flask(__name__) # Initializes flask application
app.config.from_pyfile('config.cfg') # loads application testing config from config.cfg
db = MongoEngine(app) # sets the mongoengine database to db
moment = Moment(app) # initializes flask-moment
CsrfProtect(app) # initializes CSRF protection for forms
mail = Mail(app) # allows mail to be sent

app.jinja_env.globals["len"] = len # allow len to be used in templates
app.jinja_env.globals["now"] = datetime.utcnow # sets the now variable in templates
app.jinja_env.globals["str"] = str # allows str to be used in templates
app.jinja_env.globals["moment"] = _moment # ghetto hack for something

#Importing all of the files for the project
from application import login
from application import home
from application import signup
from application import dashboard
from application import settings
from application import post
from application import judge
from application import follow
from application import flag
from application import moderators
from application import errors
from application import forgotpassword
from application import monsters
from application import verifyemail
from application import information

# API import and other things pertaining to the API
from api import api, ViewPosts, apiUrlWrap, Me

api.add_resource(ViewPosts, apiUrlWrap('/posts/<string:user>'), apiUrlWrap('/posts'))
api.add_resource(Me, apiUrlWrap('/me'))
