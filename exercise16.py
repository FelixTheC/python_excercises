#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:56:04 2019

@author: felix
"""
import time
import gc

def checktime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = (time.time() - start) * 3600
        print(f'{func.__name__}\t{end}')
        return f
    return wrapper

@checktime
def magic_tuples(_sum, max_num):
    x = max_num - 1
    while x > 0:
        if x < max_num and _sum - x < max_num:
            yield (_sum - x, x)
        x -= 1    
        
@checktime
def magic_tuples2(_sum, max_num):
    x = max_num - 1
    while x > 0:
        if _sum - x < max_num and x < max_num:
            yield (_sum - x, x)
        x -= 1   
        
        
if __name__ == '__main__':
    for i in range(10, 100):
        magic_tuples(i,i)
        
        gc.collect()
        magic_tuples2(i,i)