#!/usr/bin/env python3
"""Contains serialization and deserialization using XML
as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire en XML et l'enregistre
    dans le fichier donné."""
    # Créer l'élément racine
    root = ET.Element("data")

    # Ajouter chaque élément du dictionnaire comme enfant de l'élément racine
    for key, value in dictionary.items():
        # Créer un élément enfant avec le nom de la clé
        child = ET.SubElement(root, key)
        # Définir le texte de l'élément enfant
        child.text = str(value)  # Convertir la valeur en chaîne de caractères

    # Écrire l'arbre XML dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Désérialise les données XML d'un fichier
    et renvoie un dictionnaire Python."""
    # Analyser le fichier XML
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruire le dictionnaire à partir des éléments XML
    result_dict = {}
    for child in root:
        # Utiliser le nom de l'élément comme clé et son texte comme valeur
        result_dict[child.tag] = child.text

    return result_dict
