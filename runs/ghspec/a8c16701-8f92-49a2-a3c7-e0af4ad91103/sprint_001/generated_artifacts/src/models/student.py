from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for declarative models
Base = declarative_base()

class Student(Base):
    """Represents a student entity in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier
    name = Column(String, nullable=False)  # Name of the student, required field

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"