#!/usr/bin/python3
"""
    Module to execute the function that print a text..
"""


def text_indentation(text):
    """
        Function that prints a text with 2 new lines
        after each of these characters: ., ? and :
    """

    cont = 0
    str1 = ""
    leng = len(text)
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        for i in text:
            cont = cont + 1;
            if i != " ":
                flag = 0
            if flag == 0:
                str1 = str1 + i
            if (i == ".") or (i == "?") or (i == ":"):
                print("{:s}\n".format(str1))
                flag = 1
                str1 = ""
            if(leng) == cont:
                print("{:s}".format(str1), end="")
