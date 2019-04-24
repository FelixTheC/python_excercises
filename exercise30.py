#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 24.04.19
@author: felix
"""

# @betterrepr
# class Foo(object):
# def __init__(self, x, y):
#     self.x = x
#     self.y = y
#
# f = Foo(10, [1,2,3,4,5])
# print(f)
# I want my "betterrepr" decorator to modify __repr__ such that the output from the above code will be:
#
# Instance of Foo, vars = {'x': 10, 'y': [1, 2, 3, 4, 5]}


def betterrepr(cls):
    def repr(self):
        return f'Instance of {self.__class__.__name__}, vars={vars(self)}'
    cls.__repr__ = repr

    def inner(*args, **kwargs):
        obj = cls(*args, **kwargs)
        return obj
    return inner


if __name__ == '__main__':
    @betterrepr
    class Foo(object):

        def __init__(self, x, y):
            self.x = x
            self.y = y

    f = Foo(10, [1, 2, 3, 4, 5])
    print(f)
