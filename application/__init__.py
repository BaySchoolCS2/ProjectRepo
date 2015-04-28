from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = MongoEngine(app)

app.jinja_env.globals["len"] = len


from application import login
from application import home
from application import signup
from application import dashboard
from application import settings

from application.api import api, ViewPosts, apiUrlWrap, Me

api.add_resource(ViewPosts, apiUrlWrap('/posts/<string:user>'), apiUrlWrap('/posts'))
api.add_resource(Me, apiUrlWrap('/me'))


# @app.errorhandler(404)
# def page_not_found():
#     return render_template("errorpages/404.html"), 404
