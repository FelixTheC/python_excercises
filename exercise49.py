#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.08.19
@author: felix
"""
from enum import Enum


class CardSuit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


values = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']

CardValue = Enum('CardValue', ' '.join(values), start=2)


class Card:

    def __init__(self, suite: CardSuit, value: CardValue):
        self._suite = suite
        self._value = value

    @property
    def get_suite(self) -> CardSuit:
        return self._suite

    @property
    def get_value(self) -> CardValue:
        return self._value

    def __str__(self) -> str:
        return f'{self._value.name} of {self._suite.name}'

    def __repr__(self) -> str:
        return f'({self._value.name},{self._suite.name})'

    # not really needed but to prepend unforeseen sideeffects its is better to implement it
    # def __gt__(self, other) -> bool:
    #     return (self._suite.value > other.get_suite.value) or (self._value.value > other.get_value.value)

    def __lt__(self, other) -> bool:
        return (self._suite.value < other.get_suite.value) or (self._value.value < other.get_value.value)

    def __eq__(self, other) -> bool:
        return (self._suite.value == other.get_suite.value) and (self._value.value == other.get_value.value)

    # not really needed but to prepend unforeseen sideeffects its is better to implement it
    # def __ne__(self, other) -> bool:
    #     return (self._suite.value != other.get_suite.value) and (self._value.value != other.get_value.value)

    def __getitem__(self, item) -> Enum:
        if item == 0:
            return self._suite.value
        else:
            return self._value.value
