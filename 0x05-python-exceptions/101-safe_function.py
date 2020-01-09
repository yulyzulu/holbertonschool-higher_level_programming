#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct
    except ZeroDivisionError:
        return None
