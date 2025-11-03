from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///students.db")  # Default to an SQLite database if no environment variable is set

# Create the SQLAlchemy engine to connect to the database
engine = create_engine(DATABASE_URL)

# Base class for declarative models
Base = declarative_base()

def initialize_database():
    """Initializes the database by creating the required schema."""
    try:
        Base.metadata.create_all(engine)  # Create all tables based on the Base model
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error during database initialization: {e}")

# Call the function to initialize the database when the application starts
if __name__ == "__main__":
    initialize_database()