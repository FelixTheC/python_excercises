#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.06.19
@author: Reuven M. Lerner
"""


import pytest
from exercise39 import ImmutableParent, ImmutableMeansImmutableError


def test_immutable():
    class ImmutableMe(ImmutableParent):
        pass

    im = ImmutableMe(x=111, y=222, z=[10, 20, 30])
    print(f"Before, vars(im) = {vars(im)}")
    im.z[2] = 'hello'

    with pytest.raises(ImmutableMeansImmutableError) as e:
        im.x = 999
        assert 'Cannot set x' in e

    with pytest.raises(ImmutableMeansImmutableError) as e:
        im.a = 'Hello'
        assert 'Cannot set a' in e

    assert vars(im) == {'x': 111, 'y': 222, 'z': [10, 20, 'hello']}
