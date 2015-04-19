#! tools-env/bin/python

import pymongo

for user in pymongo.MongoClient().project.User.find():
    print user
