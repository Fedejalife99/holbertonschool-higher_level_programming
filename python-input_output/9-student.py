#!/usr/bin/python3
"""define a class that represent a student"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """initialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
