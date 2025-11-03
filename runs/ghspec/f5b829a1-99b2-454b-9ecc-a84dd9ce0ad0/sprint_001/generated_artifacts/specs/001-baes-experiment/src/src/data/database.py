from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Base class for SQLAlchemy models
Base = declarative_base()

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./students.db')

# Creating an engine for SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

class Student(Base):
    """Student model representing the students in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Function to initialize the database
def init_db():
    """Create the database schema if it doesn't exist."""
    Base.metadata.create_all(bind=engine)

# Session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ensure database is initialized on application startup
if __name__ == "__main__":
    init_db()