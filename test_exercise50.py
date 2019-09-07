#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.09.19
@author: Reuven M. Lerner
"""


import pytest
from exercise50 import Menu, ops


@pytest.mark.parametrize('instring,outstring', [
    ('+ 1 2', '3'),
    ('+ 5 5', '10'),
    ('+ 5 a 6 b', '11'),
    ('+ -5 5', '5')             # ignore negative numbers!
])
def test_add(capsys, instring, outstring):
    m = Menu()
    m.do_add(instring)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == f'{outstring}\n'


@pytest.mark.parametrize('instring,outstring', [
    ('- 1 2', '-1'),
    ('- 5 5', '0'),
    ('- 5 a 6 b', '-1'),
    ('- -5 5', '5')             # ignore negative numbers!
])
def test_sub(capsys, instring, outstring):
    m = Menu()
    m.do_sub(instring)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == f'{outstring}\n'


@pytest.mark.parametrize('instring,outstring', [
    ('* 1 2', '2'),
    ('* 5 5', '25'),
    ('* 5 a 6 b', '30'),
    ('* -5 5', '5')             # ignore negative numbers!
])
def test_mul(capsys, instring, outstring):
    m = Menu()
    m.do_mul(instring)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == f'{outstring}\n'


@pytest.mark.parametrize('instring,outstring', [
    ('/ 1 2', '0.5'),
    ('/ 5 5', '1.0'),
    ('/ 5 a 6 b', '0.8333333333333334'),
    ('/ -5 5', '5')             # ignore negative numbers!
])
def test_div(capsys, instring, outstring):
    m = Menu()
    m.do_div(instring)
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == f'{outstring}\n'


def test_add_nothing(capsys):
    m = Menu()
    m.do_add('')
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'Nothing to add\n'


def test_sub_nothing(capsys):
    m = Menu()
    m.do_sub('')
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'Nothing to subtract\n'


def test_mul_nothing(capsys):
    m = Menu()
    m.do_mul('')
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'Nothing to multiply\n'


def test_div_nothing(capsys):
    m = Menu()
    m.do_div('')
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'Nothing to divide\n'


def test_ops():
    assert '+' in ops
    assert '-' in ops
    assert '*' in ops
    assert '/' in ops


@pytest.mark.parametrize('instring,outstring', [
    ('+ 1 2', 'add 1 2'),
    ('- 5 3', 'sub 5 3'),
    ('* 10 2', 'mul 10 2'),
    ('/ 20 4', 'div 20 4'),
    ('mul 10 2', 'mul 10 2'),
])
def test_precmd(capsys, instring, outstring):
    m = Menu()
    result = m.precmd(instring)
    assert result == outstring


def test_eof():
    m = Menu()
    result = m.do_EOF('')
    assert result == True
