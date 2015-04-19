#! tools-env/bin/python

import pymongo
from werkzeug.security import generate_password_hash

usernames_file = open("tools/libs/usernames", "r")

users = []

for line in usernames_file:
    if not(pymongo.MongoClient().project.User.find_one({'alias':line.split(":")[0]})):
        if line.split(':')[3].strip() == 'true':
            verified = True
        else:
            verified = False
        users.append({"alias":line.split(":")[0],"email":line.split(":")[1],"password":generate_password_hash(line.split(":")[2]), "emailVerified":verified})

for user in users:
    pymongo.MongoClient().project.User.insert(user)
