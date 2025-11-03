from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """
    Student model representing a record in the students table.

    Attributes:
        id (int): The unique identifier for a student.
        name (str): The name of the student. This field is required.

    Methods:
        __repr__(): Returns a string representation of the Student instance.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        # Return a human-readable representation of the Student object
        return f"<Student(id={self.id}, name='{self.name}')>"