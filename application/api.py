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
from collections import User, Posts, Following
from flask.ext.restful import Api, Resource, reqparse
from flask import abort, request


api = Api(app)




def apiUrlWrap(url, version="v1"):
    return "/api/"+version+url

class Me(Resource):
    def get(self):
        try:
            user = User.objects.get(apiKey = request.headers.get('Authorization'))
        except db.DoesNotExist:
            abort(401, {'message': 'bad api key'})
        p = []
        try:
            for post in Posts.objects(author = user):
                p.append(post)
        except db.DoesNotExist:
            pass
        s = []

        try:
            for i in Following.objects(user = user):
                s.append(i)
        except db.DoesNotExist:
            s = []
        p1 = []
        for post in p:
            post["author"] = post["author"]["alias"]
            post.pop("score", None)
            p1.append(post)
        return {"subscriptions":s, "posts":p1}

    def post(self):
        try:
            user = User.objects.get(apiKey = request.headers.get('Authorization'))
        except db.DoesNotExist:
            abort(401, {'message':'bad api key'})

        body = request.form["data"]
        title = request.form["title"]

        p = Posts(author = user, title = title, content = body)
        p.save()

        return {"derp":"derp"}

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
                    return type(post)
                    post.pop("score", None)
                    p.append(post)
            except IndexError:
                p = None
        else:
            posts = Posts.objects()
            p = []
            for post in posts:
                p.append(post)

            for post in p:
                post["author"] = post["author"]["alias"]
                post.pop("score", None)
        return {"posts":p}
