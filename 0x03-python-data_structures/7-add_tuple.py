#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        n1 = 0
    else:
        n1 = tuple_a[0]

    if len(tuple_a) < 2:
        n2 = 0
    else:
        n2 = tuple_a[1]

    if len(tuple_b) == 0:
        n3 = 0
    else:
        n3 = tuple_b[0]

    if len(tuple_b) < 2:
        n4 = 0
    else:
        n4 = tuple_b[1]

    return(n1 + n3, n2 + n4)
