#!/usr/bin/python3
"""
    Module to execute the function that print a text..
"""


def text_indentation(text):
    """
        Function that prints a text with 2 new lines
        after each of these characters: ., ? and :
    """
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        while i < len(text):
  
            if (text[i] == ".") or (text[i] == "?") or (text[i] == ":"):
                print("{:s}\n".format(text[i]))
                if text[i + 1] == " ":
                    i += 1
                elif (text[i + 1] == ".") or (text[i + 1] == "?") or (text[i + 1] == ":"):
                    pass
            else:
                print("{:s}".format(text[i]), end="")
            i += 1