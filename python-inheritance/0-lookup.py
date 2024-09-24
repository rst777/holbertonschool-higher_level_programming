#!/usr/bin/python3
"""Module contenant la fonction lookup."""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: L'objet dont on veut obtenir les attributs et méthodes.

    Returns:
        list: Une liste contenant les noms des attributs
        et méthodes de l'objet.
    """
    return dir(obj)
