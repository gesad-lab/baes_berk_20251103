from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Database model for a Student entity."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field for email address

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"