#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        Max = my_list[0]
        for i in range(len(my_list)):
            if (Max > my_list[i]):
                Max = Max
            else:
                Max = my_list[i]
        return (Max)

    else:
        return (None)
