from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Define the base class for declarative models
Base = declarative_base()

# Define the Student model
class Student(Base):
    """Represents a student in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # name is required

# Database configuration
DATABASE_URL = "sqlite:///students.db"  # SQLite database for storing student information

# Function to initialize the database
def initialize_database():
    """Creates the database schema if it doesn't exist."""
    
    engine = create_engine(DATABASE_URL)
    
    # Create all tables defined by the models
    Base.metadata.create_all(engine)
    
    # Ensure that the engine is connected
    try:
        with engine.connect() as connection:
            print("Database connection established and initialized.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

# Initialize the database on module import
initialize_database()