#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for the_list in matrix:
        if len(the_list) == 0:
            print()
        for n in range(len(the_list)):
            print("{:d}".format(n), 
                    end = "\n" if n is len(the_list) - 1 else " ")

