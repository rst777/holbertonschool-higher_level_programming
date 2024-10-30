#!/usr/bin/python3

"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):

    """
    Lists all cities of a given state from the specified database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name
        state_name (str): Name of the state to search for

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
        cursor.execute("""
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        cities = [row[0] for row in rows]
        print(", ".join(cities))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    list_cities_by_state(username, password, database, state_name)
