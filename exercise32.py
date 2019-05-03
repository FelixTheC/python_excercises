#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 02.05.19
@author: felix
"""


class PercentageTooHighError(Exception):
    pass


class PercentageTooLowError(Exception):
    pass


class Percentage:
    percentage = {}

    def __init__(self, value=100):
        if isinstance(value, (float, int)):
            self.percentage['default'] = Percentage.__check_percentage(value)
        else:
            raise TypeError('init value must be of typ float or int')

    def __get__(self, instance, owner):
        self.percentage.setdefault(instance, self.percentage['default'])
        return int(self.percentage[instance])

    def __set__(self, instance, value):
        self.percentage[instance] = Percentage.__check_percentage(value)

    @staticmethod
    def __check_percentage(value):
        if value > 100:
            raise PercentageTooHighError('Percentage to high')
        elif value < 0:
            raise PercentageTooLowError('Percentage to low')
        else:
            return value
