#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states_with_a(username, password, database):
    """
    Lists all State objects containing the letter 'a'.

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

    # Query for State objects containing the letter 'a', ordered by id
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Check if any states were found and print the results
    if not states:
        print("Nothing")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    list_states_with_a(username, password, database)
