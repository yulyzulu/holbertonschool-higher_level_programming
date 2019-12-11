#!/usr/bin/python3
def remove_char_at(str, n):
    string = str
    string = string[:n:]
    print("{:s}".format(string),end="")
