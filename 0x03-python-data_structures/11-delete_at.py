#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        for i in range(len(my_list)):
            if idx < 0:
                return (my_list)
            elif idx > (len(my_list) - 1):
                return (my_list)
            else:
                del my_list[i]
                return (my_list)
