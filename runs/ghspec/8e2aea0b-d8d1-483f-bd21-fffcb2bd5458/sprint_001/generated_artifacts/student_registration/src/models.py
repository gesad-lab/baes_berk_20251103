from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declare a base class for declarative models
Base = declarative_base()

class Student(Base):
    """
    Student model representing a student entity in the database.

    Attributes:
        id (int): Unique identifier for the student.
        name (str): Name of the student. Should not be empty.
    """

    __tablename__ = 'students'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        # String representation of the Student object
        return f"<Student(id={self.id}, name='{self.name}')>"