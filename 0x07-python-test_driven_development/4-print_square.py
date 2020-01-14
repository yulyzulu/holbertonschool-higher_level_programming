#!/usr/bin/python3
"""
    Module to execute the function prints a square.
"""


def print_square(size):
    """
        Function that prints a square with the character #.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("{:s}".format("#"), end="")
        print()
