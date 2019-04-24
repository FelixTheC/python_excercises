#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:24:37 2018

@author: felix
"""
import pandas as pd

class TableFull(Exception):
    pass

class Person:
    
    def __init__(self, forename, surename):
        self.first = forename
        self.last = surename
        
    def __call__(self):
        return (self.first, self.last)
    
    def __str__(self):
        return f'{self.first}, {self.last}'
    
    def __repr__(self):
        return f'Person {self.first}, {self.last}'


class GuestList:
    max_at_table = 10
    
    def __init__(self):
        self.persons = []
        self.tables = {}
            
    def __len__(self):
        return len(self.persons)
    
    def __str__(self):
        text = ''
        for k, v in self.tables.items():
            persons = ''
            text += f'{k}\n'
            for p in v:
                persons += f'\t{p.last}, {p.first}\n'
            text += persons
        return text
    
    def __repr__(self):
        return 'GuestList object'
    
    def person_exists(self, person):
        return list([True for f, s in self.persons if person[0] is f and person[1] is s])

    def assign(self, person, table=None):
        if type(person) == Person:
            self.persons.append(person)
            if table in self.tables:
                if len(self.tables[table]) < 10 and table is not None:
                    self.tables[table].append(person)
                else:
                    raise TableFull(f'Table {table} is full')
            else:
                self.tables[table] = [person]
        else:
            raise TypeError(f'{person} must be of type Person')
            
    def table(self, number):
        try:
            return self.tables[number]
        except KeyError:
            raise KeyError(f'{number} not tables')
            
    def unassigned(self):
        return self.tables[None]
    
    def free_space(self):
        return dict({k: self.max_at_table - len(v) for k, v in self.tables.items()})
    
    def guests(self):
        tables = []
        person = []
        for key, value in self.tables.items():
            for val in value:
                tables.append(key)
                person.append(val)
        dic = {'table': pd.Series(tables),
               'person': pd.Series(person)}
        df = pd.DataFrame.from_dict(dic, orient='index').transpose()
        df['f_name'] = df.person.apply(lambda x: x.first)
        df['l_name'] = df.person.apply(lambda x: x.last)
        df = df.sort_values(by=['table', 'l_name', 'f_name'])
        return list(df.person.values)
            
            
if __name__ == '__main__':
    pass