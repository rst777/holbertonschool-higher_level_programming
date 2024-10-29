#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states_N(username, password, database):
    """
    Lists all states with a name starting with N (upper N)
    from the specified database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        )

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            if row[1][0] == 'N':
                print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_N(username, password, database)
