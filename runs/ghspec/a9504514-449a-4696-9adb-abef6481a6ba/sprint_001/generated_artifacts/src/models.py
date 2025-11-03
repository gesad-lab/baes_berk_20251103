from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instantiate the declarative base for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """
    Represents a student entity in the database.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student. Must be unique and not null.
    """

    __tablename__ = 'students'  # Name of the table in the database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    name = Column(String, nullable=False)  # Student name, cannot be null

    def __repr__(self):
        """
        String representation of the Student object.
        """
        return f"<Student(id={self.id}, name={self.name})>"