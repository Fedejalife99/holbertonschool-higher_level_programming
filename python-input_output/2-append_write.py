#!/usr/bin/python3
"""function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """funtion"""
    with open(filename, "a", encoding="utf-8") as file:
        filetxt = file.write(text)
        return filetxt
