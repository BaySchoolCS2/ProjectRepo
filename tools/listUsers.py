#! tools-env/bin/python

from mongoengine import connect, Document, EmailField, StringField, BooleanField, DateTimeField

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
    color = StringField(required=True)
    emailVerifyKey = StringField()

connect(db='project',
    host = 'localhost',
    port = 27017)

for user in User.objects:
    print user["alias"], user["email"]
