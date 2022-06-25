#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Function to divide each number in a matrix by a particular number
    """
    answer = 0
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            for j in i:
                if type(j) is not int and type(j) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len1 = len(matrix[0])
    for i in matrix:
        if len(i) != len1:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    return new_matrix
