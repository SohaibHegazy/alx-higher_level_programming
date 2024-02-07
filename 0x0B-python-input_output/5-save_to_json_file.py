#!/usr/bin/python3
""" Module to write to file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    with open('filename', 'w') as f:
        json.dump(my_obj, f)
