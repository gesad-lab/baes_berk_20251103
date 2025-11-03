from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Model representing a student entity in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    email = Column(String, nullable=False, unique=True)  # New required field for email

    def __init__(self, name: str, email: str):
        """
        Initializes a new Student instance.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.
        """
        self.name = name
        self.email = email

    def __repr__(self):
        """Represent the Student object as a string."""
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"