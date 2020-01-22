#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        if attrs is None
            return self.__dict__

        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    for st in attrs:
                        try:
                            getattr(...)
                        except:
                            continue

