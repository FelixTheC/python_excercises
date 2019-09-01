#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.08.19
@author: felix
"""
from enum import Enum


class CardSuit(Enum):
    HEARTS = 0x01
    DIAMONDS = 0x10
    CLUBS = 0x20
    SPADES = 0x30


values = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']

CardValue = Enum('CardValue', ' '.join(values), start=2)


class Card:

    def __init__(self, suite: CardSuit, value: CardValue):
        self._suite = suite
        self._value = value
        self._total_val = value.value * suite.value

    @property
    def get_total_val(self) -> int:
        return self._total_val

    def __str__(self) -> str:
        return f'{self._value.name} of {self._suite.name}'

    def __repr__(self) -> str:
        return f'({self._value.name},{self._suite.name})'

    # not really needed but to prepend unforeseen sideeffects its is better to implement it
    def __gt__(self, other) -> bool:
        return self.get_total_val > other.get_total_val

    def __lt__(self, other: 'Card') -> bool:
        return self.get_total_val < other.get_total_val

    def __eq__(self, other: 'Card') -> bool:
        return self.get_total_val == other.get_total_val

    # not really needed but to prepend unforeseen sideeffects its is better to implement it
    def __ne__(self, other) -> bool:
        return self.get_total_val != other.get_total_val

    def __getitem__(self, item: int) -> Enum:
        if item == 0:
            return self._suite.value
        else:
            return self._value.value
