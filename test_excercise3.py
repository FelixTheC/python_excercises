#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:37:38 2018

@author: Reuven M. Lerner
"""

#!/usr/bin/env python3

import excercise3

logfilename = "mini-access-log.txt"


def test_read_logs():
    log_list = excercise3.logtolist(logfilename)
    assert len(log_list) == 206


def got_a_list():
    log_list = excercise3.logtolist(logfilename)
    assert type(log_list) is list


def all_are_dicts():
    log_list = excercise3.logtolist(logfilename)
    assert all([type(x) is dict for x in log_list])


def test_check_keys():
    log_list = excercise3.logtolist(logfilename)
    assert set(log_list[0].keys()) == {"ip_address", "timestamp", "request"}


def test_check_values():
    log_list = excercise3.logtolist(logfilename)
    first_log_dict = log_list[0]

    assert first_log_dict["ip_address"] == "67.218.116.165"
    assert first_log_dict["timestamp"] == "30/Jan/2010:00:03:18 +0200"
    assert first_log_dict["request"] == "GET /robots.txt HTTP/1.0"