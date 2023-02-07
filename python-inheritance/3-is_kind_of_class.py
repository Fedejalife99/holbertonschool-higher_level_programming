#!/usr/bin/python3
"""function that verify if an object is an instance of a class or child"""


def is_kind_of_class(obj, a_class):
    """return True if if it is an instance of false if not"""
    if isinstance(obj, a_class):
        return True
    return False
