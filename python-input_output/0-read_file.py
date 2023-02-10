#!/usr/bin/python3
"""define a function that read a file"""


def read_file(filename=""):
    """fucntion that read a file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
