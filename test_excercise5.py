#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:41:06 2018

@author: Reuven M. Lerner
"""

import excercise5 as solution
import csv

filename = 'cities.csv'

def test_writes_1000_cities():
    solution.cities_to_csv(solution.gist_url, filename)

    for index, one_row in enumerate(csv.reader(open(filename))):
        pass

    assert index == 999

def test_each_city_has_four_fields():
    solution.cities_to_csv(solution.gist_url, filename)

    all_lines_have_four = [len(fields) == 4
                           for fields in csv.reader(open(filename), delimiter='\t')]
        
    assert all(all_lines_have_four)

def test_first_is_new_york():
    solution.cities_to_csv(solution.gist_url, filename)

    city, state, rank, population = open(filename).readline().strip().split('\t')

    assert city == 'New York'
    assert state == 'New York'
    assert rank == '1'
    assert population == '8405837'

def test_last_is_panama_city():
    solution.cities_to_csv(solution.gist_url, filename)

    for fields in csv.reader(open(filename), delimiter='\t'):
        pass

    city, state, rank, population = fields

    assert city == 'Panama City'
    assert state == 'Florida'
    assert rank == '1000'
    assert population == '36877'