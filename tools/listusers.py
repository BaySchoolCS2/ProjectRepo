#! tools-env/bin/python

import pymongo

users = pymongo.MongoClient().project.User.find()

for user in users:
    print user
