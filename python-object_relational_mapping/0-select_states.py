#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
It connects to a MySQL server running on localhost at port 3306
and retrieves states ordered by states.id in ascending order.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to the MySQL database and retrieves all states ordered by id.

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
            db=database, port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all results
        states = cursor.fetchall()

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
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
