#!/usr/bin/python3
"""Module contenant la fonction is_same_class."""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance de la classe spécifiée.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer.

    Returns:
        bool: True si obj est exactement une instance de a_class,
              False sinon.
    """
    return type(obj) is a_class
