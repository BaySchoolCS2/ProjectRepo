from application import db

class User(db.Document):
    email = db.EmailField(required=True)
    alias = db.StringField(required=True)
    password = db.StringField(required=True)
    emailVerified = db.BooleanField(default=False)
    lastLogin = db.DateTimeField()
    allowTracking = db.BooleanField(default=False)

class Posts(db.Document):
    #max length of title is 140 characters
    title = db.StringField(required=True, max_length=140)
    author= db.ReferenceField(User)
    #max length of content is 10000 characters
    content= db.StringField(max_length=10000)
    score = db.IntField(default=0)

class Following(db.Document):
    user = db.ReferenceField(User)
    following = db.ListField(db.ReferenceField(User))

class Kicked(db.Document):
    alias = db.StringField(required=True)
    ends = db.DateTimeField(required=True)

class Banned(db.Document):
    email = db.EmailField(required=True)
