from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData
from sqlalchemy.schema import CreateTable

# Base class for models
Base = declarative_base()

# Define Course model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Migration script for creating courses table
def migrate_courses(engine):
    """Create the courses table in the database."""
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    # Example usage: replace 'sqlite:///example.db' with your actual database URL
    engine = create_engine('sqlite:///student_management.db')

    # Initialize migration
    migrate_courses(engine)