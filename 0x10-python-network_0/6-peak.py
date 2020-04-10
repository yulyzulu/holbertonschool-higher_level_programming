#!/usr/bin/python3
""" Module to execute function"""


def find_peak(list_of_integers):
    """ Find_peak function"""
    if list_of_integers:
        sort_list = sorted(list_of_integers)
        return sort_list[-1]
    else:
        return None
