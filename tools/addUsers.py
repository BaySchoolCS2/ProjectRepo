#! tools-env/bin/python

from mongoengine import connect, Document, EmailField, StringField, BooleanField, DateTimeField
from werkzeug.security import generate_password_hash

usernames_file = open("tools/libs/usernames", "r")

users = []

class User(Document):
    email = EmailField(required = True, unique = True)
    alias = StringField(required = True, unique = True)
    password = StringField(min_length = 8, required = True)
    emailVerified = BooleanField(default = False)
    lastLogin = DateTimeField()
    allowTracking = BooleanField(default = False)
    isMod = BooleanField(default = False)

for line in usernames_file:
    for line in usernames_file:
        pw_hash = generate_password_hash(line.split(":")[2])
        try:
            User(email=line.split(":")[1], alias=line.split(":")[0], password=pw_hash, isMod=line.split(":")[3]).save()
        except:
            print "failed to create user %s" % line.split(":")[0]
