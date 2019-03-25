#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:31:02 2018

@author: felix
"""

import pytest
import myrange_exercise2 as myra

def test_myrange2_is_a_list():
    output = myra.myrange2(10)
    assert type(output) is list

@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10,20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10,20,2))),
    (10, 20, 3, list(range(10,20,3)))
])
def test_myrange2(first, second, third, output):
    if third:
        assert myra.myrange2(first, second, third) == output
    else:
        assert myra.myrange2(first, second) == output

def test_myrange3_is_a_generator():
    output = myra.myrange3(10)
    assert iter(output) is output

@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10,20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10,20,2))),
    (10, 20, 3, list(range(10,20,3)))
])
def test_myrange3(first, second, third, output):
    if third:
        assert list(myra.myrange3(first, second, third)) == output
    else:
        assert list(myra.myrange3(first, second)) == output
        

if __name__ == '__main__':
    pytest.main()