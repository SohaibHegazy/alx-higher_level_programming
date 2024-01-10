#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = 0
    best_k = ""
    for k, v in a_dictionary.items():
        if v > best:
            best = v
            best_k = k
    return best
