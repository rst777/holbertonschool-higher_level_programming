#!/usr/bin/env python3

import os

def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Erreur : Le template doit être une chaîne de caractères.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Erreur : La liste des participants doit être une liste de dictionnaires.")
        return

    # Vérification des entrées vides
    if not template.strip():
        print("Le template est vide, aucun fichier de sortie généré.")
        return
    if not attendees:
        print("Aucune donnée fournie, aucun fichier de sortie généré.")
        return

    # Traitement de chaque participant
    for index, attendee in enumerate(attendees, start=1):
        # Création d'une copie du template pour chaque participant
        invitation = template

        # Remplacement des placeholders
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            if value is None:
                value = 'N/A'
            invitation = invitation.replace(f"{{{key}}}", str(value))

        # Génération du fichier de sortie
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as file:
            file.write(invitation)

        print(f"Fichier {output_filename} généré avec succès.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Lecture du template depuis un fichier
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des participants
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Appel de la fonction avec le template et la liste des participants
    generate_invitations(template_content, attendees)
