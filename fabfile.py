#! /usr/bin/python

from fabric.api import local

def update_reqs():
    '''Updates requirements.txts'''
    local('./utils/upgrade.sh')

def setup_env():
    '''sets up environment'''
    local('./utils/setup.sh')
