from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Student model to represent the students in the database."""

    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each student
    name = Column(String, nullable=False)  # Name of the student, cannot be null

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"