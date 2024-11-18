#!/usr/bin/env python3
"""Python built-in classes extention module"""


class VerboseList(list):
    """A class built upon the list default class"""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)

    def pop(self, position = -1):
        if position == -1 or position < len(self):
            print(f"Popped [{self[position]}] from the list.")
            super().pop(position)
