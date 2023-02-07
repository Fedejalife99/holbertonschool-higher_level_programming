#!/usr/bin/python3
"""funtion that verify if a object inherit from a parent class"""


def inherits_from(obj, a_class):
    """return true if inherit from a parent or false if not"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
