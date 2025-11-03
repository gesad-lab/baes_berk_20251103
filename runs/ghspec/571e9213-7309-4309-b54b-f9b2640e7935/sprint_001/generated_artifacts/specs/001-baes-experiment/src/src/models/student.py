from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """Represents a student entity in the database."""
    
    __tablename__ = 'students'

    # Primary key, auto-incremented
    id = Column(Integer, primary_key=True, autoincrement=True)  
    # Required name field
    name = Column(String, nullable=False)  

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"