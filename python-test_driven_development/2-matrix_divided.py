#!/usr/bin/python3
"""
This module contains a function for dividing all elements of a matrix.

The main function in this module is matrix_divided, which takes a matrix
(as a list of lists) and a divisor, and returns a new matrix with all
elements divided by the divisor.
"""


def matrix_divided(matrix, div):

    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with all elements divided by div,
                       rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix is not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
"""
    # Vérification du type de `matrix`
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Vérification de la taille uniforme des lignes
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification du type de chaque élément dans `matrix`
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    # Vérification du type et de la valeur de `div`
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Création de la nouvelle matrice avec les valeurs divisées et arrondies
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
