from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

def init_db() -> None:
    """
    Initialize the database and run migrations by creating the necessary tables.
    If the tables already exist, no action is taken.
    """
    # Import the models here to ensure they are registered with the Base metadata
    from src.models.student import Student
    
    # Create the database tables if they do not already exist
    Base.metadata.create_all(bind=engine)

# Run the database initialization when this script is executed
if __name__ == "__main__":
    init_db()