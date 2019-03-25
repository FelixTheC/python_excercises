#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from exercise15 import checkpickle, fields
from glob import glob
from io import StringIO
import time
import pickle

just_quit_input = StringIO('q\n')
add_one_person_input = StringIO('a\nfirst1\nlast1\n1111@\nq\n')
add_two_people_input = StringIO('a\nfirst1\nlast1\n1111@\na\nfirst2\nlast2\n2222@\nq\n')
add_two_people_and_list = StringIO('a\nfirst1\nlast1\n1111@\na\nfirst2\nlast2\n2222@\nl\nq\n')

def test_just_quit(monkeypatch, tmp_path):
    monkeypatch.setattr('sys.stdin', just_quit_input)
    test_stem = tmp_path / 'test-cp'
    checkpickle(cp_stem=test_stem)
    assert glob(f'{test_stem}*') == []

def test_add_one_person(monkeypatch, tmp_path):
    monkeypatch.setattr('sys.stdin', add_one_person_input)
    test_stem = tmp_path / 'test-cp'
    checkpickle(cp_stem=test_stem)
    assert len(glob(f'{test_stem}*')) == 1

def test_add_two_people(monkeypatch, tmp_path):
    monkeypatch.setattr('sys.stdin', add_two_people_input)
    test_stem = tmp_path / 'test-cp'
    checkpickle(cp_stem=test_stem)
    assert len(glob(f'{test_stem}*')) == 1

def test_add_two_people_and_list(capsys, monkeypatch, tmp_path):
    monkeypatch.setattr('sys.stdin', add_two_people_and_list)
    test_stem = tmp_path / 'test-cp'
    checkpickle(cp_stem=test_stem)
    captured_out, captured_err = capsys.readouterr()
    outlines = captured_out.split('\n')
    # assert len(outlines) == 3
    print(outlines)
    assert 'Enter your choice: last1, first1: email 1111@' in outlines
    assert 'last2, first2: email 2222@' in outlines

def test_glob_has_timestamp(monkeypatch, tmp_path):
    add_two_people_and_list.seek(0)
    monkeypatch.setattr('sys.stdin', add_two_people_and_list)
    test_stem = tmp_path / 'test-cp'
    checkpickle(cp_stem=test_stem)
    assert len(glob(f'{test_stem}*{int(time.time())}*')) == 1

def test_file_contains_pickled_list_of_dicts(monkeypatch, tmp_path):
    add_two_people_and_list.seek(0)
    monkeypatch.setattr('sys.stdin', add_two_people_and_list)
    test_stem = tmp_path / 'test-cp'
    checkpickle(cp_stem=test_stem)
    filename = glob(f'{test_stem}*{int(time.time())}*')[0]
    people = pickle.load(open(filename, 'rb'))
    assert type(people) == list
    assert all([type(one_person) == dict
                for one_person in people])
    assert all([set(one_person.keys()) == set(fields)
                for one_person in people])