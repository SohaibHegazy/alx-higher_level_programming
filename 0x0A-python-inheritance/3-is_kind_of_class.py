#!/usr/bin/python3
""" check the type Module """


def is_kind_of_class(obj, a_class):
    """
    function to check if type matches

    Args:
    obj: the object to compare
    a_class: the class to compare to

    Return: true if matches and false otherwise
    """
    return isinstance(obj, a_class)
