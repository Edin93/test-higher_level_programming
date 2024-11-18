#!/usr/bin/env python3
"""Basic Abstract Class Module"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal Abstract Base Classe"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog subclass from Animal ABC"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass from Animal ABC"""

    def sound(self):
        return "Meow"
