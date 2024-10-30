#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def add_state(username, password, database):
    """
    Adds the State object "Louisiana" to the specified database.

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

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to save changes to the database
    session.commit()

    # Print the new state's ID after creation
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    add_state(username, password, database)
