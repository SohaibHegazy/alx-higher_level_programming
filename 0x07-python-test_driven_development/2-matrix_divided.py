#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ divides all elements of matrix

    Args:
    matrix: the matrix
    div: the integer to divide by

    Raise:
    TypeError if not numbers or floats
    TypeError if each list is not of the same size
    ZeroDivisionError if div is zero

    Return: new matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    for L in matrix:
        if len(L) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        if len(L) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")

        if not isinstance(L, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")

        for n in L:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

    return [[round(n/div, 2) for n in L] for L in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
