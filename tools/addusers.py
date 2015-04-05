#! tools-env/bin/python

import pymongo
from werkzeug.security import generate_password_hash #werkzeug is a dependency for flask it is installed if flask is installed

usernames_file = open("tools/libs/usernames", "r")

users = []

for line in usernames_file:
    if not(pymongo.MongoClient().project.User.find_one({'alias':line.split(":")[0]})):
        if line.split(':')[3].strip() == 'true':
            verified = True
        else:
            verified = False
        users.append({"alias":line.split(":")[0],"email":line.split(":")[1],"password":generate_password_hash(line.split(":")[2]), "emailVerified":verified})
#check_password_hash would be used to check passwords (if you used this you would then have to also import check_password_hash from werkzeug.security)
#example: http://flask.pocoo.org/snippets/54/

for user in users:
    pymongo.MongoClient().project.User.insert(user)
