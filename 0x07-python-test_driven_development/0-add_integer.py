#!/usr/bin/python3
"""
    Module to execute the function add 2 integers.
"""


def add_integer(a, b=98):
    """
        Function that adds 2 integers.
    """
    if a != a:
        return float('NaN')
    if b != b:
        return float('NaN')
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
