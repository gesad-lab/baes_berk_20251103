# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base class for declarative class definitions
Base = declarative_base()

def get_database_session(database_url: str):
    """
    Creates a new SQLAlchemy database session.

    :param database_url: The database URL for the SQLite database.
    :return: A new database session.
    """
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    return Session()

def init_db(database_url: str):
    """
    Initializes the database with the required tables.

    :param database_url: The database URL for the SQLite database.
    """
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)  # Create tables based on models defined in Base
