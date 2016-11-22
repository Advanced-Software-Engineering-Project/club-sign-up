#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:27:08 2016

@author: peng
"""

from fabric.api import local

def prepare_deploy():
    local("pylint server.py") # STATIC TEST
    local("python test.py") # DYNAMIC UNITTEST
    local("git add -p && git commit --allow-empty") # PRE BUILD
    local("git push") # BUILD