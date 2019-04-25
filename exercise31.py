#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 24.04.19
@author: felix
"""


def betterrepr(newrepr=None, newstr=None):

    def wrapper(cls):
        def _repr(self):
            return f'Instance of {self.__class__.__name__}, vars = {vars(self)}'

        cls.__repr__ = newrepr if newrepr is not None else _repr
        if newstr is not None:
            cls.__str__ = newstr

        def inner(*args, **kwargs):
            obj = cls(*args, **kwargs)
            return obj
        return inner

    return wrapper
