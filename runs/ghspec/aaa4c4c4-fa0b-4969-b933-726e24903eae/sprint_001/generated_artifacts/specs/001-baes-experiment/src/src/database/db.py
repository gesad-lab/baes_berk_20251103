import os
import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for declarative models
Base = declarative_base()

class Student(Base):
    """ Student data model. """
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

def create_connection():
    """ Create a database connection to the SQLite database specified by db_file.
    
    Returns:
        Connection object or None
    """
    db_file = os.getenv("DATABASE_URL", "sqlite:///students.db")
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to database '{db_file}' successful.")
        return conn
    except Error as e:
        print(f"Error '{e}' occurred while connecting to database.")
        return None

def create_schema():
    """ Create the database schema for the students table if it doesn't exist. """
    engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///students.db"))
    Base.metadata.create_all(engine)
    print("Database schema created successfully.")

def get_session():
    """ Creates a new session for database operations.
    
    Returns:
        Session object
    """
    engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///students.db"))
    Session = sessionmaker(bind=engine)
    return Session()

# Run this when the module is executed to create the schema
if __name__ == "__main__":
    create_schema()