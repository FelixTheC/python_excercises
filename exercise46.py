#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.08.19
@author: felix
"""
from typing import List, Tuple


def mymypy(parameter: List[any]) -> any:
    def wrapper(func):
        def inner(*args, **kwargs):
            if compare_paramaters_type(parameter, args):
                result = func(*args, **kwargs)
            else:
                raise TypeError(f'You must use {parameter}')
            return result
        return inner
    return wrapper


def compare_paramaters_type(a: List[any], b: Tuple[any]) -> bool:
    for origin, base in zip(a, b):
        if not isinstance(base, origin):
            return False
    return True
