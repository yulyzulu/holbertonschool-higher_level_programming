#!/usr/bin/python3
""" Module to execute function"""
def find_peak(list_of_integers):
    """ Find_peak function"""
    len_list = len(list_of_integers)
    mid = (0 + len_list) / 2
    if list_of_integers is not None:       
        for i in range(len(list_of_integers) - 1):
            if (list_of_integers[mid] > list_of_integers[mid + 1] and list_of_integers[mid] > list_of_integers[mid + 1]):
                return mid

    else:
        return None   





# for i in range(list_of_integers):
            #if list_of_integers[0] > list_of_integers[1]:
            #    return 0
  #          if (list_of_integers[i] > list_of_integers[i] - 1 and list_of_integers[i] > list_of_integers[i] + 1):
 #               print(i)     
   # else:
    #    return None
