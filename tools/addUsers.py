#! tools-env/bin/python

from mongoengine import connect, Document, EmailField, StringField, BooleanField, DateTimeField
from werkzeug.security import generate_password_hash

usernames_file = open("tools/libs/usernames", "r")

users = []

connect(db='project',
    host = 'localhost',
    port = 27017)

class User(Document):
    email = EmailField(required = True, unique = True)
    alias = StringField(required = True, unique = True)
    password = StringField(min_length = 8, required = True)
    emailVerified = BooleanField(default = False)
    lastLogin = DateTimeField()
    allowTracking = BooleanField(default = False)
    isMod = BooleanField(default = False)
    apiKey = StringField()
    isJudge = BooleanField(default=False)
    hasJudgeKey = BooleanField(default=False)
    judgeKey = StringField()

for line in usernames_file:
    for line in usernames_file:
        print line
        pw_hash = generate_password_hash(line.split(":")[2])
        User(email=line.split(":")[1], alias=line.split(":")[0], password=pw_hash, isMod=line.split(":")[3], isJudge=line.split(":")[4]).save()
