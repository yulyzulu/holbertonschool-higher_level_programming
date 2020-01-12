#!/usr/bin/python3
def matrix_divided(matrix, div):
    length = len(matrix[0])
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    for i in matrix:
        if type(i) != list or type(i) != int and type(i) != float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if length != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 
            return (list(map(lambda i: list(map(lambda j: round(j / div, 2), i)), matrix)))
