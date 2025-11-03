```python
import os
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base for declarative model classes
Base = declarative_base()

class DatabaseConnection:
    """
    Handles database connection, schema creation, and session management.
    """

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.create_schema()

    def create_schema(self):
        """
        Creates the database schema if it does not exist.
        """
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """
        Provides a new session. It's important that the session is used in a context manager.
        
        Returns:
            session: A new session object for database operations.
        """
        return self.Session()

def initialize_database():
    """
    Initialize the SQLite database with the database URL from the environment variable or default.
    """
    db_url = os.getenv('DATABASE_URL', 'sqlite:///students.db')
    db_connection = DatabaseConnection(db_url)
    return db_connection

# Model for Student entity
class Student(Base):
    """
    Defines the Student entity with the "name" attribute using SQLAlchemy ORM.
    """
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"
```