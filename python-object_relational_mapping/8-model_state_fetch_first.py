#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_first_state(username, password, database):
    """
    Prints the first State object from the specified database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name

    Returns:
        None
    """
    # Create the connection string
    connection_string = (
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    # Create an engine
    engine = create_engine(connection_string)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for the first State object by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if a state was found and print the result
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    print_first_state(username, password, database)
