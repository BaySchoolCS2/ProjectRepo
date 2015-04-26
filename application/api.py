"""
    This is going to confuse anyone who has ever used a restful interface before
    If you do not know what a restful interface is then you should not go any
    further.

    As a further explanation this is a pitiful attempt to make a way for a computer
    to easily interface with the website. The beauty of it is that there is no
    ui needed, instead requests are responded to with json and http errors. If
    any of that made sense to you then take a look.
"""

from application import app, db
from collections import User, Posts
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
            posts = Posts.objects(author = user)  # returns a list of posts by alias
            titles = ''
            for post in posts:
                titles += post.title + ', '
            titles = titles[0:len(titles)-2]
        except IndexError:
            titles = None

        return {"username":user.alias, "posts":titles}
