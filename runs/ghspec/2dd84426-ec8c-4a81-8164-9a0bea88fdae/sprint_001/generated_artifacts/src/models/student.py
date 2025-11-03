from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student entity in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # The name of the student, must be provided on creation.

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student(id={self.id}, name={self.name})>"