# src/models/teacher.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Model representing a Teacher entity in the educational management system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        """Return a string representation of the Teacher instance."""
        return f'<Teacher(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>'

    @classmethod
    def create_teacher(cls, session, first_name: str, last_name: str, email: str):
        """
        Create a new Teacher instance and add it to the database session.

        :param session: The database session to use for the transaction.
        :param first_name: The first name of the teacher.
        :param last_name: The last name of the teacher.
        :param email: The email address of the teacher.
        :raises ValueError: If any required fields are missing or invalid.
        """
        if not first_name or not last_name or not email:
            raise ValueError("All fields must be provided: first_name, last_name, email.")
        
        new_teacher = cls(first_name=first_name, last_name=last_name, email=email)
        session.add(new_teacher)
        return new_teacher


# src/models/__init__.py

# Existing import statements
from .student import Student
from .course import Course
from .teacher import Teacher  # New Teacher import

