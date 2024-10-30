#!/usr/bin/python3
"""
Module containing the State class definition and Base configuration
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class representing the 'states' table in the MySQL database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        String representation of the State object
        """
        return f"<State(id={self.id}, name='{self.name}')>"


if __name__ == "__main__":
    from sqlalchemy import create_engine

    # Connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://root:1207@localhost:3306/hbtn_0e_6_usa',
        pool_pre_ping=True)

    # Create tables in the database
    Base.metadata.create_all(engine)
