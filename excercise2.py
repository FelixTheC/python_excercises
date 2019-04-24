#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:45:03 2018

@author: felix
"""

class SlicableDict(dict):
    """
    Returns a key a list of keys or raise an KeyError
    """
    
    def __getitem__(self, index):
        """
        index: a single key -> 'foo', more keys combined 'foobar...' or a list of
        keys -> ['foo', 'bar', ...]
        """
        if type(index) != list:
            if index in self:
                try:
                    return self.get(index)
                except TypeError:
                    raise KeyError(f'No such key {index}')
            else:
                return [self.__getitem__(i) if i in self else None for i in index]
        else:
            return [self.__getitem__(i) if i in self else None for i in [j for j in index]]


if __name__ == '__main__':
    dic = SlicableDict({'a': 23, 'b':3, 'c':8765})
    print(dic[['a', 'b', 'd']])
    print(dic['abd'])