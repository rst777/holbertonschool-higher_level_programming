#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
It connects to a MySQL server running on localhost at port 3306
and retrieves states ordered by states.id in ascending order.
"""

import MySQLdb
import sys


def list_states_with_n(username, password, database):
    """
    Connects to the MySQL database and retrieves
    all states with names starting with 'N'.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database to connect to.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to get states starting with 'N'
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE 'N%' "
            "ORDER BY id ASC"
        )
        print("Executing query: ", query)  # Impression pour débogage
        cursor.execute(query)  # Exécutez la requête
        states = cursor.fetchall()  # Récupère les résultats

        # Vérifie si des états ont été retournés
        if not states:
            print("No states found with names starting with 'N'.")
        else:
            # Print results
            for state in states:
                print(state)

        # Close the cursor and the connection
        cursor.close()
        db.close()

    except MySQLdb.OperationalError as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)


if __name__ == "__main__":
    list_states_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
