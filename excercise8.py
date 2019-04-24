#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:36:44 2018

@author: felix
"""
from random import choice


def create_math_problems(func):
    numbers = get_numbers(-40, 40)
    calculus = ['-', '+']
    with func as file:
        for i in range(1, 101):
            text_arr = [choice(numbers), choice(calculus), f'( {choice(numbers)} )',
                        choice(calculus), f'( {choice(numbers)} )',
                        choice(calculus), f'( {choice(numbers)} )']
            text = ' '.join(text_arr)
            file.write(f'[{i}] {text} = _________ \n')
    

def solve_math_problems(func):
    with func as file:
        for line in file:
            text_arr = line.strip().split(' ')
            text_arr[-1] = str(get_line_result(text_arr))
            print(' '.join(text_arr))
            
def get_line_result(line):
    braces = ['(', ')']
    #calculus = {'+': '__add__', '-': '__sub__'}
    line = list([i for i in line[1: -2] if i not in braces ])
    return eval(''.join(line))
#    line = list([int(i) if i.lstrip('-').isnumeric() else calculus[i] for i in line])
#    a = line[0].__getattribute__(line[1])(line[2])
#    b = line[4].__getattribute__(line[5])(line[6])
#    return a.__getattribute__(line[3])(b)


def get_numbers(minimum, maximum):
    if minimum < 0:
        nums1 = list([str((i * -1))  for i in range(minimum * -1)])
        _ = list([str(i) for i in range(maximum)])
        nums1.extend(_)
    else:
        nums1 = list([str(i) for i in range(minimum, maximum)])
    return nums1


if __name__ == '__main__':
    solve_math_problems(open('test.txt', 'r+'))