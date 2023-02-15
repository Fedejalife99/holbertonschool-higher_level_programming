#!/usr/bin/python3
"""define a class to be the base from all the excersises"""
import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return that returns the JSON string representation"""
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
