#!/usr/bin/python3
'''
Module to execute the functions
'''
import json


class Base:
    """ Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save file Method"""
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            json_str = cls.to_json_string(new_list)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(json_str)
        elif list_objs is None:
            f.write(new_list)

    @staticmethod
    def from_json_string(json_string):
        """From json string Method """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create Method """
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 3)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
