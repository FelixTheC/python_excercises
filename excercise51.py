#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 14.09.19
@author: felix
"""
import threading
from queue import PriorityQueue
from typing import List, Tuple


def worker(func, args, q):
    q.put(func(*args))


def threadify(func: any, args: List[Tuple]) -> List:
    q = PriorityQueue()
    results = []
    threads = []
    for i in args:
        x = threading.Thread(target=worker, args=(func, i, q))
        threads.append(x)
        x.start()
    for t in threads:
        t.join()
        results.append(q.get())
    return results

#
# if __name__ == '__main__':
#     def add(x, y):
#         return x + y
#
#     def rand_slow_add(a, b):
#         time.sleep(random.randint(0, 5))
#         return a + b
#
#     print(threadify(add, [(1, 2), (3, 4), (5, 6)]))
#     # print(threadify2(rand_slow_add, [(1, 2), (3, 4), (5, 6)]))