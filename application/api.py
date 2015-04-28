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
from collections import User, Posts
from flask.ext.restful import Api, Resource, reqparse
from flask import abort, request

api = Api(app)

parser = reqparse.RequestParser
parser.add_argument('Auth', type=str, location='headers')


def apiUrlWrap(url, version="v1"):
    return "/api/"+version+url

class Me(Resource):
    def get(self):
        pass


class ViewPosts(Resource):
    def get(self, user=None):
        if user != None:
            try:
                user = User.objects(alias = user)[0]
            except IndexError:
                abort(404)
            try:
                posts = Posts.objects(author = user)
                p = []
                for post in posts:
                    post["author"] = post["author"]["alias"]
                    post.pop("score", None)
                    p.append(post)

            except IndexError:
                posts = None
            return {"posts":p}
        else:
            posts = Posts.objects()
            p = []
            for post in posts:
                p.append(post)

            for post in p:
                post["author"] = post["author"]["alias"]
                post.pop("score", None)
            return {"posts":p}
