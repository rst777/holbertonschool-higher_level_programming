#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convertit un fichier CSV en JSON et l'écrit dans data.json"""
    try:
        # Ouverture et lecture du fichier CSV
        with open(csv_filename, mode='r', newline='', encoding='utf-8')\
                as csv_file:
            # Utilisation de DictReader pour
            # transformer chaque ligne en dictionnaire
            csv_reader = csv.DictReader(csv_file)

            # Conversion des données en liste de dictionnaires
            data = [row for row in csv_reader]

        # Écriture des données JSON dans le fichier data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{csv_filename}' est introuvable.")
        return False

    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        return False


result = convert_csv_to_json('data.csv')

if result:
    print("Conversion réussie.")
else:
    print("La conversion a échoué.")
