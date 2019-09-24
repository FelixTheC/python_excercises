#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 14.09.19
@author: felix
"""


from excercise51 import threadify
import time
import random


def add(a, b):
    return a + b


def rand_slow_add(a, b):
    time.sleep(random.randint(0, 5))
    return a + b


input_list = [(10, 3),
              (20, 4),
              (30, 5)]


def test_simple_func():
    output = threadify(add, input_list)

    assert output == [add(*one_arg)
                      for one_arg in input_list]


def test_slow_func():
    output = threadify(rand_slow_add, input_list)

    assert output == [rand_slow_add(*one_arg)
                      for one_arg in input_list]
