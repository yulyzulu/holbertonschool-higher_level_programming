#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        string = str[:n] + str[1 + n:]
        return (string)
    else:
        return(str)
