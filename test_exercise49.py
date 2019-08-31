#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.08.19
@author: Reuven M. Lerner
"""


from exercise49 import Card, CardSuit, CardValue
from random import shuffle


def test_all_suits():
    assert len(list(CardSuit)) == 4


def test_a_value():
    assert len(list(CardValue)) == 13


def test_one_card():
    new_card = Card(CardSuit.SPADES, CardValue.TWO)
    assert str(new_card) == 'TWO of SPADES'


def test_two_cards():
    low_card = Card(CardSuit.SPADES, CardValue.TWO)
    high_card = Card(CardSuit.SPADES, CardValue.THREE)
    assert low_card < high_card
    assert high_card > low_card


def test_two_suits():
    low_card = Card(CardSuit.HEARTS, CardValue.TWO)
    high_card = Card(CardSuit.SPADES, CardValue.TWO)
    assert low_card < high_card
    assert high_card > low_card


def test_sort_cords():
    origin_cards = list([Card(i, j) for i in list(CardSuit) for j in list(CardValue)])
    cards = list([Card(i, j) for i in list(CardSuit) for j in list(CardValue)])
    for i in range(5):
        shuffle(cards)
    assert any(oc != c for oc, c in zip(origin_cards, cards))
    cards.sort(key=lambda x: (x[0], x[1]))
    assert all(oc == c for oc, c in zip(origin_cards, cards))
