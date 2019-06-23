#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.06.19
@author: felix
"""
import abc


class ImmutableMeansImmutableError(Exception):
    pass


class ImmutableParent(abc.ABC):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            # mark each attribute as property helps to prevend changes from mutable objects like lists or strings
            self.__dict__[k] = property(v)

    def __setattr__(self, key, value):
        if key in self.__dir__():
            raise ImmutableMeansImmutableError(f'Cannot change {key}')
        else:
            raise ImmutableMeansImmutableError(f'Cannot add {key}')
