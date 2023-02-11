#!/usr/bin/python3
"""Defines a function that converts python objects into a dictionary"""


def class_to_json(obj):
    """function"""
    return obj.__dict__
