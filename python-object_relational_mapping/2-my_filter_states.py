#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import sys
import MySQLdb
from sys import argv


def search_states(username, password, database, state_name):

    """
        Displays all values in the states table where name matches
        the argument.

        Args:
            username (str): MySQL username
            password (str): MySQL password
            database (str): Database name
            state_name (str): State name to search for

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
            ("SELECT * FROM states WHERE BINARY name = '{}' "
                "ORDER BY id ASC").format(argv[4])
        )

        # Fetch all the rows
        rows = cursor.fetchall()

        # Displays the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySql Error:", e)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(
            argv[0]))
        exit(1)

    username, password, database, state_name = sys.argv[1:]
    search_states(username, password, database, state_name)
