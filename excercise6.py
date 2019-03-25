#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:46:30 2018

@author: felix
"""
import numpy as np
from collections import Counter
from itertools import chain

all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
               {'name':'Atara', 'age':17, 'hobbies':['horses', 'cooking', 'art', 'reading']},
               {'name':'Shikma', 'age':15, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
               {'name':'Amotz', 'age':13, 'hobbies':['biking', 'cooking']},
               ]

def average_age_under(list_dict, age=0):
    if age is 0:
        res = np.mean([x['age'] for x in list_dict])
    else:
        res = np.mean([x['age'] for x in list_dict if x['age'] < age])
    return 0 if np.isnan(res) else res

def all_hobbies(list_dict):
    if len(list_dict) < 1:
        return set()
    return set(list(chain(*[i['hobbies'] for i in all_people])))

def hobby_counter(list_dict):
    if len(list_dict) < 1:
        return Counter()
    return Counter(list(chain(*[i['hobbies'] for i in all_people])))

def n_most_common(list_dict, n_common=0):
    if len(list_dict) < 1:
        return list()
    res = list(chain(*[i['hobbies'] for i in all_people]))
    if n_common is 0:
        return list(Counter(res).keys())
    else:
        return list(Counter(res).keys())[:n_common]
    
    
if __name__ == '__main__':
    all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
               {'name':'Atara', 'age':17, 'hobbies':['horses', 'cooking', 'art', 'reading']},
               {'name':'Shikma', 'age':15, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
               {'name':'Amotz', 'age':13, 'hobbies':['biking', 'cooking']},
               ]
    print(n_most_common(all_people, 3))
