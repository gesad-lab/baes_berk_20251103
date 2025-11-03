from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define a base class for declarative class definitions
Base = declarative_base()

class Student(Base):
    """Student model to represent a student entity in the database."""

    __tablename__ = 'students'  # Name of the table in the SQLite database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each student
    name = Column(String, nullable=False)  # Student's name, which is required

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student(id={self.id}, name='{self.name}')>"