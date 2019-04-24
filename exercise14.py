#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 22:48:30 2018

@author: felix
"""

class ThresholdEqual(int):
    threshold = 2
    
    def __eq__(self, obj):
        x = self.numerator - obj.numerator
        if x < 0:
            x *= -1
        return 0 <= x <= self.threshold
    
    
if __name__ == '__main__':
    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(11)
    te3 = ThresholdEqual(6)
    print(te1 == te1)
    print(te2 == te3)