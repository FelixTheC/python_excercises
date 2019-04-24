#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:03:03 2019

@author: felix
"""


class Foo(object):
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return True if self.x == other.x else False

    def __hash__(self):
        return hash(self.x)


class Uniquish(object):
    def __eq__(self, other):
        a = self.__dict__.items() >= other.__dict__.items()
        b = self.__dict__.items() <= other.__dict__.items()
        return a - b == 0

    def __hash__(self):
        return hash(self.__dict__.values())
