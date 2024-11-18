#!/usr/bin/env python3
"""Iter function extended class module"""


class CountedIterator:
    """Custom iterator class that counts the iterator items"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            self.counter += 1
            item = next(self.iterator)
            return item
        except Exception:
            raise StopIteration
