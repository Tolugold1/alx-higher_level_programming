#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_lenght = len(matrix)
    for i in range(matrix_lenght):
        for j in range(len(matrix[0])):
            print("{}".format(matrix[i][j]), end='')
            if j + 1 < len(matrix[0]):
                print(" ", end='')
        print()
