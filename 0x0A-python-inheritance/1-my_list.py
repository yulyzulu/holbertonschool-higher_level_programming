#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        list1 = list.copy(self)
        if type(list1) == list:
            list1.sort()
            print(list1)
