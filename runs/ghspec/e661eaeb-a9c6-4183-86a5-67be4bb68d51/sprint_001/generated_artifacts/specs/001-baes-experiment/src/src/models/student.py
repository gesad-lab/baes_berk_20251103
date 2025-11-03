from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for declarative model definitions
Base = declarative_base()

class Student(Base):
    """
    Represents a Student entity in the database.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student.
    """

    __tablename__ = 'students'  # Define the table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each student
    name = Column(String, nullable=False)  # Student's name, must be provided

    def __repr__(self):
        """
        Returns a string representation of the Student instance.
        """
        return f"<Student(id={self.id}, name='{self.name}')>"