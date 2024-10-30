#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_state_by_name(username, password, database, state_name):
    """
    Prints the State object with the specified name.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name
        state_name (str): Name of the state to search for

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

    # Query for the State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Check if a state was found and print the result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> "
              "<database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    print_state_by_name(username, password, database, state_name)
