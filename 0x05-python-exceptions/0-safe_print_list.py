#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i in range(0, x):
            if x < 0:
                return 0
            else:
                print("{:d}".format(my_list[i]), end="")
                j = j + 1
        print()
        return (j)
    except (IndexError, TypeError):
        print()
        return j
