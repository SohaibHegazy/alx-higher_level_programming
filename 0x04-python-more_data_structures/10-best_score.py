#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_v = 0
    best_k = None
    for k, v in a_dictionary.items():
        if v > best_v:
            best_v = v
            best_k = k
    return best_k
