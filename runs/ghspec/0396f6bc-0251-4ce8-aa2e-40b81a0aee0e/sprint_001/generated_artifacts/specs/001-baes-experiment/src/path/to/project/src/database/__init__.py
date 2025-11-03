```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define the base model for the database
Base = declarative_base()

class Student(Base):
    """Represents a student entity in the database."""

    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Student name must not be null

def initialize_database(db_url: str):
    """Initializes the database and creates the required tables if they don't exist.

    Args:
        db_url (str): The database URL for the SQLite connection.
    """
    # Create database engine
    engine = create_engine(db_url, echo=True)  # Set echo=True for SQL logging, useful during development
    # Create all tables
    Base.metadata.create_all(engine)

# Define the database URL, defaulting to a local SQLite database
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./students.db')

# Initialize the database upon module startup
initialize_database(DATABASE_URL)
```