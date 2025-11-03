from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models.student import Base

# Database URL - Adjust accordingly based on environment (use .env file in production)
DATABASE_URL = 'sqlite:///students.db'

def create_database():
    """Create the SQLite database and the students table if it doesn't exist."""
    try:
        # Create an engine that connects to the SQLite database
        engine = create_engine(DATABASE_URL)

        # Create all tables in the database that are defined by Base's subclasses
        Base.metadata.create_all(engine)
        print("Database created and tables created successfully.")
    except SQLAlchemyError as e:
        # Log and handle errors while creating the database
        print(f"Error occurred while creating the database: {str(e)}")

# Entry point for database creation
if __name__ == "__main__":
    create_database()