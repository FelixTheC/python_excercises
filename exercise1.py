#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:55:48 2018

@author: felix
"""
def read_n(filename, linenumber=1):
    length = 0
    with open(filename, 'r+') as _:
        length = len(_.readlines())
    with open(filename, 'r+') as file:
        for _ in range(int(length/linenumber)):
            for i in range(linenumber):
                yield file.readline().rstrip()
            else:
                yield ''


if __name__ == '__main__':
    for i in read_n('requirements.txt', 4):
        print(i)