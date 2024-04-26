#!/usr/bin/python3
'''
a function that finds a peak in a list of unsorted integers.
'''


def find_peak(list_of_integers):
    '''
    Function to find a peak of a list
    '''

    if not list_of_integers:
        return None

    list_len = len(list_of_integers)
    start = 0
    end = list_len - 1

    while start < end:
        mid = int(list_len / 2)
        if list_of_integers[mid] > list_of_integers[mid - 1] and\
                list_of_integers[mid] > list_of_integers[mid + 1]:
                    return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
