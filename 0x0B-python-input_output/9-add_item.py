#!/usr/bin/python3
from sys import argv
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    Mylist = load_from_json_file('add_item.json')

except:
    Mylist = []

finally:

    for i in range(1, len(argv)):
        Mylist.append(argv[i])
    save_to_json_file(Mylist, 'add_item.json')
