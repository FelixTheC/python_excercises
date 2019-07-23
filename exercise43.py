#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.07.19
@author: felix
"""
import sqlite3


def create_appointments_table(conn: sqlite3.Connection) -> sqlite3.Cursor:
    """
    table_name -- appointments
    title -- name of the appointment
    starts_at -- date and time of when it starts
    ends_at -- date and time of when it ends
    comment -- not surprisingly, comments and notes about the appointment
    """
    db_query = '''create table if not exists appointments (id integer primary key,
    title TEXT,
    starts_at TIMESTAMP,
    ends_at TIMESTAMP,
    comment TEXT);'''
    return conn.execute(db_query)


def insert_one_appointment(conn: sqlite3.Connection) -> sqlite3.Cursor:
    title = input('title ')
    start = input('starts_at ')
    ends = input('ends_at ')
    comment = input('comment ')
    db_query = '''insert into appointments (title, starts_at, ends_at, comment) 
    values ('{title}', '{start}', '{ends}', '{comment}');'''.format(title=title,
                                                                    start=start,
                                                                    ends=ends,
                                                                    comment=comment)
    cursor = conn.execute(db_query)
    conn.commit()
    return cursor


def get_appointments(conn: sqlite3.Connection) -> list:
    db_query = '''select * from appointments'''
    cursor = conn.execute(db_query)
    return cursor.fetchall()
