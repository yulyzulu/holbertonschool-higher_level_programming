#!/usr/bin/python3
def matrix_divided(matrix, div):
    for i in matrix:
        if type(matrix[i]) != int and type(matrix[i]) != float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

