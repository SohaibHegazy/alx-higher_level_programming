#!/usr/bin/python3
""" function that returns the list of available attributes"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object

    Args:
    obj: the object to get its list

    Return: the list
    """
    return dir(obj)
