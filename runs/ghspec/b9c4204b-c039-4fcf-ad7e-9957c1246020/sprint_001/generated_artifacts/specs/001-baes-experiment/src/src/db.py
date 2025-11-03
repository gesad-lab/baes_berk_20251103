from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Create an engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a declarative base class
Base = declarative_base()

class Student(Base):
    """Student entity model representing the 'students' table."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create a new SQLAlchemy session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    """Initialize the database and create schema if it doesn't exist."""
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

# Call the init_db function to set up the database schema
init_db()