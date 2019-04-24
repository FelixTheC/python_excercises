#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:49:45 2019

@author: felix
"""
import pickle
import time

people = []
run = True
    
def checkpickle(cp_stem='people-checkpoint-'):
    
    def choice():
        commands = {'q': 'Quit from the program (function)',
                    'l': 'List all people in the address book',
                    'a': 'Add a new person to the address book',
                    'r': 'Restore the address book to the stage from a specific timestamp\n-> ',
                    }
        _ = [f'{k}: {v}' for k, v in commands.items()]
        while True:
            cmd = input('\n'.join(_))
            if cmd.lower() in commands.keys():
                return cmd
    
    def _quit():
        global run
        run = False
            
    def _list():
        for enum, dic in enumerate(people):
            try:
                print(enum)
                for key, val in dic.items():
                    print(f'\t{key}: {val}')
            except AttributeError:
                pass
            
    def _add_new_person(path):
        person = dict()
        for field in fields():
            person[field] = input(f'{field}: ').strip()
        people.append(person)
        path_with_time = f'{path}{int(time.time())}.pickle'
        with open(path_with_time, 'wb') as file:
            pickle.dump(people, file)
        
    def _restore(path):
        global people
        timestamp = input('Enter timestamp: ')
        path_with_time = f'{path}{timestamp}.pickle'
        with open(path_with_time, 'rb') as file:
            people = pickle.load(file)
        
    cmd_func = {'q': _quit,
                'l': _list,
                'a': _add_new_person,
                'r': _restore,
                }
        
    while run:
        c = choice()
        if c in ['a', 'r']:
            cmd_func[c](cp_stem)
        else:
            cmd_func[c]()

    
def fields():
    return ['first_name', 'last_name', 'email']


if __name__ == '__main__':
    checkpickle()