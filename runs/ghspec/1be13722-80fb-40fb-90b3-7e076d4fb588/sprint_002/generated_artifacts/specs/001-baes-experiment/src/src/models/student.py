# /src/models/student.py

from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

    def __init__(self, name: str, email: str):
        """
        Initialize a new Student instance.

        :param name: Name of the student
        :param email: Email of the student
        """
        self.name = name
        self.email = email

    def __repr__(self):
        """
        Represent the Student instance as a string.

        :return: String representation of the Student
        """
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"