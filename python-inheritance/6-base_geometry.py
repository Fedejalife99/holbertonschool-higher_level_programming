#!/usr/bin/python3
"""define an empty class"""


class BaseGeometry:
    """empty class"""
    def __init__(self):
        pass
    def area(self):
        raise Exception("area() is not implemented")
