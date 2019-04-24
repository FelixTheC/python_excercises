#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 22:34:41 2018

@author: felix
"""

import random

class RandMemory:
    
    def __init__(self, start, stop):
        self.lowest = start
        self.highest = stop
        self._history = []
    
    @property
    def get(self):
        x = random.randint(self.lowest, self.highest)
        self._history.append(x)
        return x
    
    def history(self):
        return self._history