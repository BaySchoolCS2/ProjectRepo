## Collections.py
## This file holds all the definitions for the mongodb collections
##
## User holds the users information
##
## Comment holds the comment document. comment is a embedded document
##
## Post holds all the data from posts
##
## Subscriptions people that you follow
##
## Kicked stores people who are kicked
##
## Banned stores users who are banned

from application import db
import datetime
import uuid


class User(db.Document):
    email = db.EmailField(required = True, unique = True)
    alias = db.StringField(required = True, unique = True)
    password = db.StringField(min_length = 8, required = True)
    emailVerified = db.BooleanField(default = False)
    lastLogin = db.DateTimeField()
    allowTracking = db.BooleanField(default = False)
    isMod = db.BooleanField(default = False)
    apiKey = db.StringField()
    isJudge = db.BooleanField(default=False)
    hasJudgeKey = db.BooleanField(default=False)
    judgeKey = db.StringField()
    color = db.StringField(required=True)
    emailVerifyKey = db.StringField()
    resetPasswordCode = db.StringField()

class Inquery(db.Document):
    user = db.ReferenceField(User)
    reporters = db.ListField(db.ReferenceField(User))


class Comment(db.EmbeddedDocument):
    commentid = db.StringField(required=True)
    created_at = db.DateTimeField(required=True)
    author = db.ReferenceField(User)
    body = db.StringField(max_length=1000, required=True)
    flags = db.IntField(default=0)
    flagTypes = db.ListField(db.IntField())
    invisible = db.BooleanField(default=False)
    moderated = db.BooleanField(default=False)
    moderatedBy = db.ListField(db.ReferenceField(User))


class Posts(db.Document):
    postid = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow(), required=True)
    #max length of title is 140 characters
    title = db.StringField(required = True, max_length = 140)
    author = db.ReferenceField(User)
    #max length of content is 10000 characters
    content = db.StringField(max_length = 10000)
    score = db.IntField(default = 0)
    sticky = db.BooleanField(default = False)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))
    votedUp = db.ListField(db.ReferenceField(User))
    votedDown = db.ListField(db.ReferenceField(User))
    flags = db.IntField(default=0, required=True)
    flagTypes =  db.ListField(db.IntField())
    flaggedBy = db.ListField(db.ReferenceField(User))
    invisible = db.BooleanField(default=False)
    moderated = db.BooleanField(default=False)
    moderatedBy = db.ListField(db.ReferenceField(User))
    meta = {
        'allow_inheritance': True
    }

class Subscriptions(db.Document):
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
    subscriptions = db.ListField(db.ReferenceField(User))

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
