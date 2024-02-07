#!/usr/bin/python3
""" Module to make JSON"""


import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)

    Args:
    my_obj: the object to be serialized

    raise: nothing

    return: the serialized string
    """
    return json.dumps(my_obj)
