from application import db
import datetime

class User(db.Document):
    email = db.EmailField(required = True, unique = True)
    alias = db.StringField(required = True, unique = True)
    password = db.StringField(min_length = 8, required = True)
    emailVerified = db.BooleanField(default = False)
    lastLogin = db.DateTimeField()
    allowTracking = db.BooleanField(default = False)
    isMod = db.BooleanField(default = False)
    apiKey = db.StringField()

class Comment(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    author = db.ReferenceField(User)
    body = db.StringField(max_length=1000, required=True)

class Posts(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    #max length of title is 140 characters
    title = db.StringField(required = True, max_length = 140)
    author = db.ReferenceField(User)
    #max length of content is 10000 characters
    content = db.StringField(max_length = 10000)
    score = db.IntField(default = 0)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))
    meta = {
        'allow_inheritance': True
    }



class Following(db.Document):
    '''
        hack for getting around the fact that there cannot be self referencing classes
        i.e. class user():
            ...
            follower = db.referenceField(User)
        creates a new collection that references User instead
        stupid, yes
        neccessary, yes
        is there a better way, probably but im lazy
    '''
    user = db.ReferenceField(User)
    following = db.ListField(db.ReferenceField(User))

class Kicked(db.Document):
    '''stores temporary locks on user accounts'''
    user = db.ReferenceField(User)
    start = db.DateTimeField(required = True)
    ends = db.DateTimeField(required = True)
    reason = db.StringField(max_length = 1000)

class Banned(db.Document):
    '''stores emails of people who are not allowed to make accounts'''
    email = db.EmailField(required = True)
    reason = db.StringField(max_length = 1000)
