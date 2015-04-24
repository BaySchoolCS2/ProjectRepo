#! /usr/bin/python

from fabric.api import local

def update_reqs():
    '''Updates requirements.txts'''
    print "I have bricked upgrades because of an issue with pymongo. Do not use it"
    # local('./utils/upgrade.sh')

def setup_env():
    '''sets up environment'''
    local('./utils/setup.sh')
