#!/usr/bin/python3
"""define a function that writes an Object to a text file using Json"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename, 'w') as file:
        """function"""
        json.dump(my_obj, file)
