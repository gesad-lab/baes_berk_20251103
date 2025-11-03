from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """SQLAlchemy model for the Student entity."""
    
    __tablename__ = 'students'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)  # Name is a required field.

    def __repr__(self):
        return f"<Student(name={self.name})>"