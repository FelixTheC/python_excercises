#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:36:54 2019

@author: felix
"""
from string import punctuation as p

def create_password_checker(*args):
    """
    pos_0: min_uppercase
    pos_1: min_lowercase
    pos_2: min_punctuation
    pos_3: min_digits
    """
    parameters = args
    functions = [('uppercase', 'isupper'), ('lowercase', 'islower'),
                 ('digits', 'isdigit')]
    punctuation = list([i for i in p])

    def helper(val, func):
        return sum(list([1 for i in val if i.__getattribute__(func)()]))

    def check(args):
        result_dic = {'uppercase': parameters[0] * -1,
                      'lowercase': parameters[1] * -1,
                      'punctuation': parameters[2] * -1,
                      'digits': parameters[3] * -1}
        for i, param in enumerate(parameters):
            if i == 3:
                result_dic['punctuation'] += sum(
                        list([1 for i in args if i in punctuation]))
            else:
                result_dic[functions[i][0]] += helper(args, functions[i][1])
        check_res = [True if i >= 0 else False for i in result_dic.values()]
        return (True if False not in check_res else False, result_dic)
    return check


if __name__ == '__main__':
    pc = create_password_checker(1,2,3,4)
    result, details = pc('Abc!@#1234')
    print(result, details)