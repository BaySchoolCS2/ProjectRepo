#! tools-env/bin/python

import pymongo

usernames_file = open("tools/libs/usernames", "r")

users = []

for line in usernames_file:
    users.append({"alias":line.split(":")[0],"email":line.split(":")[1],"password":line.split(":")[2].strip()})

for user in users:
    pymongo.MongoClient().project.User.insert(user)
