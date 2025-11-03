from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

# Setup base class for SQLAlchemy models
Base = declarative_base()

# Database configuration loading from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Setup the Engine
engine = create_engine(DATABASE_URL)

# Configure session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Student(Base):
    """A model representing a student."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

def init_db():
    """Create the database schema if it does not exist."""
    try:
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError as e:
        # Log the error context
        print(f"Failed to create the database schema: {e}")
        raise

# Initialize the database schema on startup
init_db()