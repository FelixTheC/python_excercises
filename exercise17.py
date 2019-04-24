#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 09:33:26 2019

@author: felix
"""


class Item:
    
    def __init__(self, quantity, measure, name, price):
        self.quantity = quantity
        self.measure = measure
        self.name = name
        self.price = price
    
    def __str__(self):
        item = f'{self.quantity:>5} {self.measure} {self.name}'
        low = f'@ ${(lambda x: x*1.0)(self.price)}...'
        high = f'${(lambda x, y: (x*y)*1.0)(self.price, self.quantity)}'
        price = f'{low:>15}{high}'
        return f'{item} {price}'
    

class Cart:
    
    def __init__(self):
        self.items = []
        
    def add(self, item):
        if isinstance(item, Item):
            raise TypeError('item must be of Item instance')
        self.items.append(item)
        
    def __format__(self, val):
        if val == 'short':
            return ', '.join(list([i.name for i in self.items[::-1]]))
        elif val == 'long':
            return '\n'.join(list([str(i) for i in self.items[::-1]]))
        else:
            return ''
