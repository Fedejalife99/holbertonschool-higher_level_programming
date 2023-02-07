#!/usr/bin/python3
"""define a function that compares the methods and attributes of two objects"""


def is_same_class(obj, a_class):
    """returns true if they are the same and false if not"""
    if type(obj) == a_class:
        return True
    else:
         return False