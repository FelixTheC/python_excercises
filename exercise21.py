#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:05:02 2019

@author: felix
"""

def mygetter(*args):
    def inner(x):
        if len(args) < 2:
            return x[args[0]]
        else:
            return tuple([x[i] for i in args])
    return inner