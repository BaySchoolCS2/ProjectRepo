#! tools-env/bin/python

from mongoengine import connect, Document, EmailField, StringField, BooleanField, DateTimeField

connect(db='project',
    host = 'localhost',
    port = 27017)

class User(db.Document):
    email = db.EmailField(required = True, unique = True)
    alias = db.StringField(required = True, unique = True)
    password = db.StringField(min_length = 8, required = True)
    emailVerified = db.BooleanField(default = False)
    lastLogin = db.DateTimeField()
    allowTracking = db.BooleanField(default = False)
    isMod = db.BooleanField(default = False)

class Posts(db.Document):
    #max length of title is 140 characters
    title = db.StringField(required = True, max_length = 140)
    author = db.ReferenceField(User)
    #max length of content is 10000 characters
    content = db.StringField(max_length = 10000)
    score = db.IntField(default = 0)

alias = raw_input('alias: ')

title = raw_input('title: ')

content = raw_input('post (must be under 1000 characters): ')

try:
    user = User.object(alias=alias)[0]  # returns user object by alias
    post = Posts(user=user, title=title, content=content)

    post.save()
    
except IndexError:
    print('Failed to find user %s', alias)
