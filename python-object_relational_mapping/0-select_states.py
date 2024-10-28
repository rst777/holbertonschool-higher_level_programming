#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments depuis la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        user="root",  # ou 'nouvel_utilisateur' si vous avez créé un nouvel utilisateur
        password="1207",  # Assurez-vous que c'est correct
        database="hbtn_0e_0_usa"
    )

    # Création d'un curseur pour exécuter des requêtes
    cursor = db.cursor()

    # Exécution de la requête pour sélectionner tous les états
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération et affichage des résultats
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
