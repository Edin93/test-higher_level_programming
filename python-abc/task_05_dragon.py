#!/usr/bin/env python3
"""Mixins task module"""


class SwimMixin:
    """A Mixin class to add the swimming capability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """A Mixin class to add the flying capability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class defining a dragon"""

    def roar(self):
        print("The dragon roars!")
