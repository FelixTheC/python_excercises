#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Reuven M. Lerner
"""

import pytest
from exercise32 import Percentage
from exercise32 import PercentageTooLowError
from exercise32 import PercentageTooHighError


def test_default_is_100():
    class Foo:
        participation = Percentage()

    f = Foo()
    assert f.participation == 100


def test_override_default():
    class Foo:
        participation = Percentage(30)

    f = Foo()
    assert f.participation == 30


def test_can_set_to_an_int():
    class Foo:
        participation = Percentage(100)

    f = Foo()
    f.participation = 35
    assert f.participation == 35

    f.participation = 70
    assert f.participation == 70

    f.participation = 80.3
    assert f.participation == 80


def test_not_too_low_or_too_high():
    class Foo:
        participation = Percentage(100)

    f = Foo()
    with pytest.raises(PercentageTooLowError):
        f.participation = -10

    with pytest.raises(PercentageTooHighError):
        f.participation = 105


def test_each_instance_own_value():
    class Foo:
        participation = Percentage(100)

    class Bar:
        participation = Percentage(100)

    f1 = Foo()
    f2 = Foo()
    f2.participation = 50
    b1 = Bar()
    b1.participation = 0
    b2 = Bar()
    b2.participation = 70
    assert f1.participation != f2.participation
    assert b1.participation != b2.participation
    assert f1.participation != b1.participation
