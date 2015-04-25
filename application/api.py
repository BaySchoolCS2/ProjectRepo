"""
    This is going to confuse anyone who has ever used a restful interface before
    If you do not know what a restful interface is then you should not go any
    furthur.
"""

from application import app

api = restful.Api(app)

class ViewPosts(restful.Resource):
    def get(self):
        return {"hello":"derp"}
