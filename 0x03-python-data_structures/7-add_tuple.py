#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (tuple_a):
        if len(tuple_a) == 1:
            new_tuple_a = (tuple_a[0], 0)
        else:
            new_tuple_a = tuple_a
    else:
        new_tuple_a = (0, 0)
    if (tuple_b):
        if len(tuple_b) == 1:
            new_tuple_b = (tuple_b[0], 0)
        else:
            new_tuple_b = tuple_b
    else:
        new_tuple_b = (0, 0)
    return (new_tuple_a[0] + new_tuple_b[0], new_tuple_a[1] + new_tuple_b[1])
