#!/usr/bin/python3
""" Module to add args to python list"""


import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

arglist = list(sys.argv[1:])

try:
    exist_data = load_from_json_file('add_item.json')
except Exception:
    exist_data = []

exist_data.extend(arglist)
save_to_json_file(exist_data, 'add_item.json')
