#!/usr/bin/python3
"""
Module to execute the functions
"""
from models.base import Base


class Rectangle(Base):
    ''' Rectangle Class  '''
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
            return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
            return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
            return self.__y

    def area(self):
        """Area method"""
        return self.__width * self.__height

    def display(self):
        """ Display Method"""
        i = "\n" * self.__y
        j = " " * self.__x
        num = j + ("#" * self.__width)
        k = (num + "\n") * (self.__height - 1)
        print(i + k + num)

    def __str__(self):
        """ Str method"""
        msgs = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return msgs.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update method"""
        variables = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            i = 0
            for x in args:
                setattr(self, variables[i], x)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary method """
        dictionary = {
                    'id': self.id,
                    'width': self.__width,
                    'height': self.__height,
                    'x': self.__x,
                    'y': self.__y
                     }
        return dictionary
