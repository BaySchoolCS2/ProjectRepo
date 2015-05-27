#! /usr/bin/python

from fabric.api import local

def update_reqs():
    '''Updates requirements.txts'''
    print "I have bricked upgrades because of an issue with pymongo. Do not use it"
    # local('./utils/upgrade.sh')

def setup_env():
    '''sets up environment'''
    local('./utils/setup.sh')

def pull():
    '''pull from remote and then try to install all requirements if they have
    changed
    '''
    local('./utils/pull.sh')

def deleteDB():
    '''
        Deletes the database
    '''
    local('./tools/deleteDB.py')

def deleteUsers():
    '''
        Deletes all users
    '''
    local('./tools/deleteDB.py')

def deleteFollowers():
    '''
        Deletes all followers
    '''
    local('./tools/deleteFollowers.py')

def deletePosts():
    '''
        Deletes all posts
    '''
    local('./tools/deletePosts.py')

def createPost():
    '''
        Create Post
    '''
    local('./tools/createPost.py')

def listUsers():
    '''
        List Users
    '''
    local('./tools/listUsers.py')
