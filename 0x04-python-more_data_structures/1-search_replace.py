#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return list(map(lambda element: search if element == replace else element), my_list)
