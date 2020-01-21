#!/usr/bin/python3
def number_of_lines(filename=""):
    line_number = 0
    with open("my_file_0.txt") as f:
        for i in f:
            line_number += 1
    return line_number
