#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.08.19
@author: felix
"""
from exercise46 import mymypy


@mymypy([int, int])
def int_param_func(a: int, b: int):
    return a + b


@mymypy([str, str])
def str_param_func(a: str, b: str):
    return a + b


@mymypy([int, str])
def mixed_param_func(a: int, b: str):
    return b * a


def test_int_param_success():
    assert int_param_func(1, 2) == 3


def test_int_param_error():
    error = None
    try:
        int_param_func(1, '2')
    except TypeError as e:
        error = e
    assert error is not None


def test_str_param_success():
    assert str_param_func('hello', 'world') == 'helloworld'


def test_str_param_error():
    error = None
    try:
        str_param_func(1, 'Hello')
    except TypeError as e:
        error = e
    assert error is not None


def test_mixed_param_success():
    assert mixed_param_func(2, 'world') == 'worldworld'


def test_str_param_error():
    error = None
    try:
        mixed_param_func('World', 'Hello')
    except TypeError as e:
        error = e
    assert error is not None
