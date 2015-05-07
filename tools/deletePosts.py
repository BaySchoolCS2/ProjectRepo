#! tools-env/bin/python
from mongoengine import connect, Document

class Posts(Document):
    pass

Uin = raw_input('This command deletes all posts.  Are you sure you want to continue [Y/n]')
Uin = Uin.lower()

if Uin in ["y", "yes", "yolo", "yolo :)"]:
    connect(db='project',
		host = 'localhost',
		port = 27017)
    Posts.drop_collection()
