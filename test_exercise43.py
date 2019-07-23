#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.07.19
@author: Reuven M. Lerner
"""

import os
import pytest
import random
import sqlite3
import string
import datetime
from exercise43 import create_appointments_table, insert_one_appointment, get_appointments
from io import StringIO


@pytest.fixture
def db_connection():
    filename = f'test-{random.sample(string.ascii_lowercase, 5)}.db'
    conn = sqlite3.connect(filename)
    yield conn
    os.unlink(filename)


@pytest.fixture
def appointments_table(db_connection):
    create_appointments_table(db_connection)


@pytest.fixture
def three_appointments():
    a1 = 'title A\n2019-Jul-15 10:00\n2019-Jul-15 12:00\nnote 1\n'
    a2 = 'title B\n2019-Jul-15 13:00\n2019-Jul-15 14:30\nnote 2\n'
    a3 = 'title C\n2019-Jul-16 10:00\n2019-Jul-16 12:00\nbig meeting\n'

    return StringIO(a1 + a2 + a3)


def test_create_table(db_connection):
    create_appointments_table(db_connection)

    q = '''SELECT name FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
        '''

    columns = {}
    for colid, colname, coltype, *rest in db_connection.execute("pragma table_info('appointments')").fetchall():
        columns[colname] = coltype

    assert set(columns.keys()) == {'id', 'title',
                                   'starts_at', 'ends_at', 'comment'}
    assert columns['title'] == 'TEXT'
    assert columns['starts_at'] == 'TIMESTAMP'
    assert columns['ends_at'] == 'TIMESTAMP'
    assert columns['comment'] == 'TEXT'


def test_inserting_one_appointment(db_connection, monkeypatch):
    create_appointments_table(db_connection)

    monkeypatch.setattr('sys.stdin', StringIO(
        'title A\n2019-Jul-15 10:00\n2019-Jul-15 12:00\nnote\n'))
    insert_one_appointment(db_connection)

    query = '''SELECT * FROM Appointments'''
    output = [db_connection.execute(query)]
    assert len(output) == 1


def test_inserting_three_appointments(db_connection, monkeypatch, three_appointments):
    create_appointments_table(db_connection)

    monkeypatch.setattr('sys.stdin', three_appointments)
    for i in range(3):
        insert_one_appointment(db_connection)

    query = '''SELECT * FROM Appointments'''
    output = [one_item
              for one_item in db_connection.execute(query)]
    assert len(output) == 3


def test_retrieve_all_appointments(db_connection, monkeypatch, three_appointments):
    create_appointments_table(db_connection)

    monkeypatch.setattr('sys.stdin', three_appointments)
    for i in range(3):
        insert_one_appointment(db_connection)

    output = get_appointments(db_connection)
    assert len(output) == 3
