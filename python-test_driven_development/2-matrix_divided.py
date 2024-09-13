#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
Divise tous les éléments d'une matrice par un nombre donné.

    Args:
    matrix (liste de listes): La matrice à diviser.
    div (int ou float): Le nombre par lequel diviser.

    Returns:
    liste de listes: Une nouvelle matrice avec tous les éléments divisés par div, arrondis à 2 décimales.

    Raises:
    TypeError: Si matrix n'est pas une liste de listes d'entiers/flottants,
               si chaque ligne de la matrice n'a pas la même taille,
               ou si div n'est pas un nombre.
    ZeroDivisionError: Si div est égal à 0.
    """
    # Vérification du type de `matrix`
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification de la taille uniforme des lignes
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification du type de chaque élément dans `matrix`
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification du type et de la valeur de `div`
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Création de la nouvelle matrice avec les valeurs divisées et arrondies
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
