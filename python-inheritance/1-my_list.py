#!/usr/bin/python3
"""define a child class from list"""


class MyList(list):
    """class from list class thats print the parent class in ascending order"""
    def print_sorted(self):
        print(sorted(self))
