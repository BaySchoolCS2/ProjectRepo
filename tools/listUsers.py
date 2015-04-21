#! tools-env/bin/python

import pymongo

for user in pymongo.MongoClient().project.user.find():
    print user
