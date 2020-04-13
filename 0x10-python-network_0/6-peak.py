#!/usr/bin/python3
""" Module to execute function"""


def find_peak(list_of_integers):
    """ Find_peak function"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
