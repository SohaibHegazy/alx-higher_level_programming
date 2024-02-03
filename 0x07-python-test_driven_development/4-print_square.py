#!/usr/bin/python3
""" prints a square of side length equal to size using #"""


def print_square(size):
    """
    prints a square of side length equal to size
    using the symbil #

    Args:
    size: the side length of the square is an integer

    Raise:
    TypeError("size must be an integer") if not an integer
    ValueError("size must be >= 0") if negative value entered

    Return:
    prints the square using #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
