#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.19
@author: Reuven M. Lerner
@modified by: felix
"""
import pickle
import csv
import json
from xml.etree import ElementTree as ET


def check_object_func(obj, filename, func='dump'):
    dic = {}
    name_lookup = filename.split('.')[-1]
    if not dic:
        dic = {i.__name__.lower()[:-5]: i for i in obj.__class__.mro()[1: -1] if i.__name__.lower() != 'serializable'}
    try:
        if func == 'dump':
            dic[name_lookup].dump(obj, filename)
        else:
            dic[name_lookup].load(obj, filename)
        check = False
    except KeyError:
        check = True
    return check


class Serializable(object):

    def dump(self, filename):
        if check_object_func(self, filename):
            with open(filename, 'wb') as file:
                pickle.dump(vars(self), file)

    def load(self, filename):
        if check_object_func(self, filename, 'load'):
            with open(filename, 'rb') as file:
                old_vars = pickle.load(file)

                for name, value in old_vars.items():
                    setattr(self, name, value)


class JSONMixin(object):
    def dump(self, filename):
        with open(filename, 'w') as file:
            json.dump(vars(self), file)

    def load(self, filename):
        with open(filename, 'r') as file:
            old_vars = json.load(file)

            for name, value in old_vars.items():
                setattr(self, name, value)


class CSVMixin(object):
    def dump(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            o = csv.writer(csvfile, delimiter='\t')
            for name, value in vars(self).items():
                o.writerow([name, value])

    def load(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            i = csv.reader(csvfile, delimiter='\t')
            for name, value in i:
                setattr(self, name, value)


class XMLMixin(object):
    def dump(self, filename):
        a = ET.Element('attributes')
        for name, value in vars(self).items():
            node = ET.SubElement(a, name, value=str(value))

        tree = ET.ElementTree(a)

        with open(filename, 'wb') as xmlfile:
            tree.write(xmlfile)

    def load(self, filename):
        with open(filename, 'rb') as file:
            tree = ET.parse(file)
            for parent in tree.iter():
                for child in parent:
                    setattr(self, child.tag, child.attrib['value'])


if __name__ == '__main__':

    class Book(Serializable, CSVMixin):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"

    b = Book("Python Workout", "Reuven Lerner", 39)
    print(b)
    b.dump('tmp/book.data')
    b.dump('tmp/book.csv')

    b2 = Book('blah title', 'blah author', 100)
    # title, author, and price now reflect disk file
    b2.load('tmp/book.data')
    print(b2)
