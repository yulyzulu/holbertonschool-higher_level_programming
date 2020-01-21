#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    cont = 1
    with open(filename, encoding='utf-8') as f:
        for line in f:
            cont += 1
        if nb_lines <= 0 or nb_lines >= cont:
            f.seek(0)
            print(f.read(), end="")
        else:
            f.seek(0)
            for i in range(nb_lines):
                print(f.readline(), end="")
