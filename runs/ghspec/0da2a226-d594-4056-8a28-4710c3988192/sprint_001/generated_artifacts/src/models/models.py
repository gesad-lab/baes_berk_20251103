from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class for our models
Base = declarative_base()

class Student(Base):
    """Model representing a student in the database."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student(id={self.id}, name='{self.name}')>"


def create_schema(engine):
    """Create the database schema for the models."""
    Base.metadata.create_all(engine)