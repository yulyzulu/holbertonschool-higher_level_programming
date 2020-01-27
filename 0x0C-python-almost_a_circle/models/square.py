#!/usr/bin/python3
"""
    Module to execute functions
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        msgs = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return msgs.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """ update method"""
        var = ["id", "size", "x", "y"]
        if len(args) != 0:
            i = 0
            for x in args:
                setattr(self, var[i], x)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary method"""
        dictionary = {
                    'id': self.id,
                    'size': self.size,
                    'x': self.x,
                    'y': self.y
                     }
        return dictionary
