#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.07.19
@author: felix
"""


def reverse_word(word):
    return word[::-1]


def unicode_map(word):
    return {letter: ord(letter) for letter in word}
