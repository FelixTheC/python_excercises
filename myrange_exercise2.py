#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:14:29 2018

@author: felix
"""
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        print((time.time() - start) /3600)
        return f
    return wrapper


@timeit
def myrange2(start=0, stop=0, step=1):
    res = []
    #swap start and stop to use myrange3(10)
    if stop is None and start > 0 or stop == 0 and start > 0:
        start, stop = 0, start
    if step is None:
        step = 1
    while start < stop:
        res.append(start)
        start += step
            
    return res

@timeit
def myrange3(start=0, stop=0, step=1):
    #swap start and stop to use myrange3(10)
    if stop is None and start > 0 or stop == 0 and start > 0:
        start, stop = 0, start
    if step is None:
        step = 1
    while start < stop:
        yield(start)
        start += step
        

if __name__ == '__main__':
    myrange2(1, 200, 2)
    myrange3(1, 200, 2)