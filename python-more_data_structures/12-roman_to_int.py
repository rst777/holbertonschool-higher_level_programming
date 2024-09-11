#!/usr/bin/python3
def roman_to_int(roman_string):
#vérifie si l'entrée est valide
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
# Dictionnaire des valeurs des chiffres romains
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
    total = 0
    prev_value = 0

    # Parcours de la chaîne de droite à gauche
    for char in roman_string:
        if char not in roman_values:
            return 0
        # Récupère la valeur du caractère romain actuel
        current_value = roman_values[char]

        # Si la valeur actuelle est inférieure à la valeur précédente,
        # on la soustrait
        if prev_value < current_value:
            total += current_value - 2 * prev_value
        else:
            # Sinon, on l'ajoute au total
            total += current_value

        # Met à jour la valeur précédente
        prev_value = current_value
    return total
