from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Student model representing a student in the database."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New Email Field, required for each Student

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"