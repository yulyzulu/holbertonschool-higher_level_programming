#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        for i in range(0, x):
            if x < 0:
                return 0
            else:
                if type(my_list[i]) == int:
                    print("{:d}".format(my_list[i]), end="")
                    j = j + 1
        print()
        return j
    except ValueError:
        print()
        return j
