"""
    This is going to confuse anyone who has ever used a restful interface before
    If you do not know what a restful interface is then you should not go any
    furthur.

    As a furthur explanation this is a pitaful attempt to make a way for a computer
    to easily interface with the website. The beauty of it is that there is no
    ui needed, instead requests are responded to with json and http errors. If
    any of that made sense to you then take a look.
"""

from application import app, db
from collections import User
from flask.ext.restful import Api, Resource
from flask import abort

api = Api(app)

def apiUrlWrap(url):
    return "/api"+url


class ViewPosts(Resource):
    def get(self, user):
        try:
            user = User.objects(alias = user)[0]
        except IndexError:
            abort(404)

        try:
            posts = collections.Posts.objects(author = User.objects(alias=user)[0])  # returns a list of posts by alias
        except IndexError:
            posts = None

        return {"username":user.alias, "posts":posts}
