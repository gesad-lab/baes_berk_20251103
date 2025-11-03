from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student entity in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)  # unique and required attribute for the student's name

# Database initialization
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)

# Create all tables in the engine (if they don't exist yet)
Base.metadata.create_all(engine)