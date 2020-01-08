#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    for i in range(list_length):
        try:
            div.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            div.append(0)
        except TypeError:
            print("wrong type")
            div.append(0)
        except IndexError:
            print("out of range")
            div.append(0)
        finally:
            pass
    return div
