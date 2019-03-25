#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:09:20 2019

@author: felix
"""
import time


class TooSoonError(Exception):
    pass


def once_per_minute(func):
    stime = 0
    def wrapper(*args, **kwargs):
        nonlocal stime
        now = time.time()
        result = now - stime
        if result >= 60.0 or result == 0.0:
            stime = time.time()
            return func(*args, **kwargs)
        else:
            raise TooSoonError(f'Wait another {60 - result} seconds')
    return wrapper

@once_per_minute
def hello(name):
    return f"Hello, {name}"
    
    
if __name__ == '__main__':
    time.sleep(60)
    print(hello('test'))
    print(hello('test2'))