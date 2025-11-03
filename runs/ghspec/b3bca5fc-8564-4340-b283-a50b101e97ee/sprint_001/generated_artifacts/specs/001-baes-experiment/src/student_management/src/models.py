from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    """Represents a student in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)  # Non-nullable field for the student's name

    def __repr__(self):
        """Provide a string representation of the Student object."""
        return f"<Student(id={self.id}, name={self.name})>"