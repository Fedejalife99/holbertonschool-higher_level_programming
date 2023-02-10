#!/usr/bin/python3
"""define a function that write a string into a text file"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, "w", encoding="utf-8") as file:
        filetext = file.write(text)
        return filetext
