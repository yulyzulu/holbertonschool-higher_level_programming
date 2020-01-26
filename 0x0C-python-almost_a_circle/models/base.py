#!/usr/bin/python3
''' Class Base '''
import json


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

#    def save_to_file(cls, list_objs):
 #       if list_objs == None:
  #          with open("list_objs.json", "w") as f:
