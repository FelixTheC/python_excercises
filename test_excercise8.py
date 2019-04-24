#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:36:21 2018

@author: Reuven M. Lerner
"""

from excercise8 import create_math_problems, solve_math_problems

def test_create_math_problems(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    create_math_problems(open(f, 'w'))

def test_solve_problems_from_file(capsys, tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    create_math_problems(open(f, 'w'))
    solve_math_problems(open(f))
    captured_out, captured_err = capsys.readouterr()
    assert len(captured_out.split('\n')) == 101