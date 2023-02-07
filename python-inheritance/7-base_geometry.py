#!/usr/bin/python3
"""define an empty class"""


class BaseGeometry:
    """empty class"""
    def __init__(self):
        pass

    def area(self):
        """not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value its an int and greater than 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
