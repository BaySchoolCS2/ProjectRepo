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
<<<<<<< HEAD
    '''
=======
<<<<<<< HEAD
    '''
=======
        '''
>>>>>>> e45ac2998a2a3d19252b7cc203e968519d1be69b
>>>>>>> 54def194b8d3f3f4c3711b075658bb96b625ba50
    local('./utils/pull.sh')
