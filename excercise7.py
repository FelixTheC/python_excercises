#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:59:09 2018

@author: felix
"""

import os

def file_length(filename):
    return os.stat(filename).st_size

def filefunc(path, func):
    success_dict = {}
    failure_dict = {}
    for root, dirs, files, rootfd in os.fwalk(path):
        for file in files:
            filename = f'{path}{os.sep}{file}'
            try:
                success_dict[file] = func(filename)
            except Exception as e:
                failure_dict[file] = e
        return success_dict, failure_dict

    

if __name__ == '__main__':
    success_dict, failure_dict = filefunc('/home/felix/Bilder', file_length)
    print(success_dict, failure_dict)