#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 22:35:32 2018

@author: Reuven M. Lerner
"""

from exercise13 import RandMemory

def test_empty():
    r = RandMemory(1, 100)
    assert r.lowest == 1
    assert r.highest == 100
    assert r._history == []
    assert r.history() == []

def test_types():
    r = RandMemory(1, 100)
    assert type(r.get) == int

def test_three():
    r = RandMemory(1, 100)
    old_numbers = [ ]
    for i in range(3):
        old_numbers.append(r.get)
    assert r.history() == old_numbers
