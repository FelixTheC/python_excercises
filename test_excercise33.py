#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Reuven M. Lerner
"""

import unittest
import os
import json
from excercise33 import Serializable, JSONMixin, XMLMixin, CSVMixin


class Book(Serializable):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f'{self.title}, by {self.author}, for {self.price}'


class BookJSON(Serializable, JSONMixin):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f'{self.title}, by {self.author}, for {self.price}'


class BookAllMixins(Serializable, JSONMixin, CSVMixin, XMLMixin):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f'{self.title}, by {self.author}, for {self.price}'


class SerializerTest(unittest.TestCase):

    filepath = 'tmp/'

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        file = os.scandir('tmp/')
        for f in file:
            os.remove(f)

    def test_only_serializer(self):
        book = Book('Python Workout', 'Reuven Lerner', 39)
        book.dump(self.filepath + 'book.pickle')
        self.assertTrue(os.path.isfile(self.filepath + 'book.pickle'))

        book2 = Book('Python Workout', 'Reuven Lerner', 200)
        self.assertEqual(book2.price, 200)
        book2.load(self.filepath + 'book.pickle')
        self.assertNotEqual(book2.price, 200)
        self.assertEqual(book.price, book2.price)

        os.remove(self.filepath + 'book.pickle')

    def test_serializer_with_jsonmixin_json_format(self):
        book = BookJSON('Python Workout', 'Reuven Lerner', 39)
        book.dump(self.filepath + 'book.json')
        self.assertTrue(os.path.isfile(self.filepath + 'book.json'))

        book2 = BookJSON('Python Workout', 'Reuven Lerner', 200)
        self.assertEqual(book2.price, 200)
        book2.load(self.filepath + 'book.json')
        self.assertNotEqual(book2.price, 200)
        self.assertEqual(book.price, book2.price)
        # check if file is really a json
        with open(self.filepath + 'book.json', 'r') as file:
            json_data = json.load(file)
        self.assertEqual(json_data['title'], 'Python Workout')
        self.assertEqual(json_data['author'], 'Reuven Lerner')
        self.assertEqual(json_data['price'], 39)

        os.remove(self.filepath + 'book.json')

    def test_serializer_with_jsonmixin_other_format(self):
        book = BookJSON('Python Workout', 'Reuven Lerner', 39)
        book.dump(self.filepath + 'book.data')
        self.assertTrue(os.path.isfile(self.filepath + 'book.data'))

        book2 = BookJSON('Python Workout', 'Reuven Lerner', 200)
        self.assertEqual(book2.price, 200)
        book2.load(self.filepath + 'book.data')
        self.assertNotEqual(book2.price, 200)
        self.assertEqual(book.price, book2.price)

        error = None
        with open(self.filepath + 'book.data', 'r') as file:
            try:
                json.load(file)
            except UnicodeDecodeError as e:
                error = e
        self.assertIsNotNone(error)
        os.remove(self.filepath + 'book.data')

    def test_serializer_with_all(self):
        book = BookAllMixins('Python Workout Test', 'Test Author', 250)
        book.dump(self.filepath + 'book.data')
        book.dump(self.filepath + 'book.csv')
        book.dump(self.filepath + 'book.json')
        book.dump(self.filepath + 'book.xml')
        self.assertTrue(os.path.isfile(self.filepath + 'book.data'))
        self.assertTrue(os.path.isfile(self.filepath + 'book.csv'))
        self.assertTrue(os.path.isfile(self.filepath + 'book.json'))
        self.assertTrue(os.path.isfile(self.filepath + 'book.xml'))

        dump_file = open(self.filepath + 'book.data')
        csv_file = open(self.filepath + 'book.csv', 'rb')
        json_file = open(self.filepath + 'book.json', 'r')
        xml_file = open(self.filepath + 'book.xml', 'r')

        error = None
        try:
            dump_file.read()
        except UnicodeDecodeError as e:
            error = e
        self.assertIsNotNone(error)
        self.assertEqual(csv_file.read(),
                         b'title\tPython Workout Test\r\nauthor\tTest Author\r\nprice\t250\r\n')
        self.assertEqual(json_file.read(),
                         '{"title": "Python Workout Test", "author": "Test Author", "price": 250}')
        self.assertEqual(xml_file.read(),
                         '<attributes><title value="Python Workout Test" /><author value="Test Author" /><price value="250" /></attributes>')  # nopep8
        dump_file.close()
        csv_file.close()
        json_file.close()
        xml_file.close()

    def test_serializer_with_all_only_csv(self):
        book = BookAllMixins('Python Workout Test csv', 'Test Author', 500)
        book.dump(self.filepath + 'book.csv')
        self.assertTrue(os.path.isfile(self.filepath + 'book.csv'))

        csv_file = open(self.filepath + 'book.csv', 'rb')
        self.assertEqual(csv_file.read(),
                         b'title\tPython Workout Test csv\r\nauthor\tTest Author\r\nprice\t500\r\n')
        csv_file.close()


if __name__ == '__main__':

    unittest.main()
