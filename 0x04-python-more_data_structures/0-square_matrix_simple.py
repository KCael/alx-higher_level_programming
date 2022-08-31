#!/usr/bin/python3
# square_matrix_simple - computes the square value of all ints if a matrix.

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for row in range(len(matrix)):
        new_matrix[row] = list(map(lambda x: x**2, matrix[row]])
    return new_matrix
