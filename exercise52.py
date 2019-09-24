#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 21.09.19
@author: felix
"""
import os


class TempFile:

    def __init__(self, *args):
        self.file = open(args[0], args[1])
        self.path = args[0]

    def __getattr__(self, item):
        return getattr(self.file, item)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        del self

    def __del__(self):
        os.remove(self.path)

    def write(self, text):
        return self.file.write(text)

    def close(self):
        return self.file.close()


if __name__ == '__main__':
    with TempFile('tmp/mytest.txt', 'w') as f:
        f.write('text')

    print('')
