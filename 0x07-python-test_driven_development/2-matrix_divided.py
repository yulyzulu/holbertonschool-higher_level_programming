#!/usr/bin/python3
def matrix_divided(matrix, div):
    length = len(matrix[0])
    for i in matrix:
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return matrix[i][j]
