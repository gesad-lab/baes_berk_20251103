from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """Represents a student in the database."""
    
    __tablename__ = 'students'  # Table name in the database
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each student
    name = Column(String, nullable=False)  # Required field for the student's name

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"