from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key for the student record
    name = Column(String, nullable=False)  # Student's name, required field

    def __repr__(self):
        """Return a string representation of the student."""
        return f"<Student(id={self.id}, name={self.name})>"