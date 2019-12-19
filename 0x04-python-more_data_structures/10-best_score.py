#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key in a_dictionary:
            maxim = max(a_dictionary, key=a_dictionary.get)
            return (maxim)
    else:
        return (None)
