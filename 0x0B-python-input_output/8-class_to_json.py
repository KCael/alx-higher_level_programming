#!/usr/bin/python3
"""Returns the dictionary description
with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary with simple data structure"""
    return obj.__dict__
