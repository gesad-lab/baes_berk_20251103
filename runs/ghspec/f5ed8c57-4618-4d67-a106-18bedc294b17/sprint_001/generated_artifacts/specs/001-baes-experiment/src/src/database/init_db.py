from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define the base class for declarative models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

def initialize_database():
    """Initialize the database and create the necessary tables."""
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    
    # Create an engine that connects to the database
    engine = create_engine(DATABASE_URL)
    
    # Create all tables in the engine (this includes the students table)
    try:
        Base.metadata.create_all(engine)
        print("Database initialized and tables created.")
    except Exception as e:
        print(f"Error initializing the database: {e}")

# This will be called on application startup
initialize_database()