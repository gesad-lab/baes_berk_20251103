from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each student
    name = Column(String, nullable=False)  # Name of the student, must not be empty

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"