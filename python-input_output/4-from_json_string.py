#!/usr/bin/python3
"""define a function that convert a Json string into a python object"""
import json


def from_json_string(my_str):
    """function"""
    return json.loads(my_str)
