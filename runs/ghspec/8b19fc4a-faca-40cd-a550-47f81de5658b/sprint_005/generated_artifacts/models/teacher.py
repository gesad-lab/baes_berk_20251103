from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Teacher model to store teacher information."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the Teacher
    name = Column(String, nullable=False)  # Required field for Teacher's name
    email = Column(String, nullable=False, unique=True)  # Required field for Teacher's email, must be unique

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"  # String representation of the Teacher object