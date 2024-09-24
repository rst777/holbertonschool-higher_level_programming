#!/usr/bin/python3
"""Module contenant la fonction is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance ou hérite d'une classe spécifiée.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer.

    Returns:
        bool: True si obj est une instance de a_class
        ou d'une classe qui en hérite,
              False sinon.
    """
    return isinstance(obj, a_class)
