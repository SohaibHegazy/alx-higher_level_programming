#!/usr/bin/python3
""" This function adds two inetegers """


def add_integer(a, b=98):
    """ adds two integers
    Args:
    a: first integer
    b: second integer

    Raises: Type error if not integer
            Type error if not float

    Return: sum of two integers
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ ==  "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
