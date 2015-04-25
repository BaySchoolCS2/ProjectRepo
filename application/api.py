"""
    This is going to confuse anyone who has ever used a restful interface before
    If you do not know what a restful interface is then you should not go any
    furthur.
"""

from application import app
from flask.ext.restful import Api, Resource

api = Api(app)

def apiUrlWrap(url):
    return "/api"+url


class ViewPosts(Resource):
    def get(self, user):
        return {"hello":user}
