from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for declarative models
Base = declarative_base()

class Student(Base):
    """Model representing a student in the student management application"""
    
    __tablename__ = 'students'  # Database table name

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique student ID
    name = Column(String, nullable=False)  # Student name, required field

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"  # Representation of the student object for debugging