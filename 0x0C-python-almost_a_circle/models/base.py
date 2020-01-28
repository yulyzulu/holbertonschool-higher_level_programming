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
        import json
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
           # json_str = cls.to_json_string(new_list)
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list))

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

    @classmethod
    def load_from_file(cls):
        """ load from file method """
        filename1 = cls.__name__ + ".json"
        try:
            with open(filename1, "r") as f:
                read = f.read
                list_dir_python = cls.from_json_string(read)
                list_instances = []
                for dir1 in list_dir_python:
                    objets = cls.create(**dir1)
                    list_instances.append(objects)
            return list_instances

        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save file Method"""
        import json
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            json_str = cls.to_json_string(new_list)
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            f.write(json_str)

    @classmethod
    def load_from_file_csv(cls):
        """ load from file method """
        filename1 = cls.__name__ + ".csv"
        try:
            with open(filename1, "r") as f:
                read = f.read
                list_dir_python = cls.from_json_string(read)
            list_instances = []
            for dir1 in list_dir_python:
                objets = cls.create(**dir1)
                list_instances.append(objects)
            return list_instances

        except:
            return []
