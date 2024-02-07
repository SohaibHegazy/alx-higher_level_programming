#!/usr/bin/python3
""" module to represent Pascal's Triangle"""


def pascal_triangle(n):
    """
    function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    p_tri = [[1]]
    while len(p_tri) < n:
        tri = p_tri[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        p_tri.append(temp)
    return p_tri
