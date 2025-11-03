import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the Base class for declarative models
Base = declarative_base()

class Student(Base):
    """Model representing a student."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"

# Database connection configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create a new database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and create the schema."""
    
    # Create the tables in the database (if they don't exist)
    Base.metadata.create_all(bind=engine)

# Call to initialize DB (for automatic schema creation on startup)
init_db()