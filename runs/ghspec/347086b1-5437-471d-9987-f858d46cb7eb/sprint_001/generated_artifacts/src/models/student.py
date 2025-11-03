from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Define the base for declarative models
Base = declarative_base()

class Student(Base):
    """Represents a student in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name of the student, cannot be null

    def __repr__(self):
        """String representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"