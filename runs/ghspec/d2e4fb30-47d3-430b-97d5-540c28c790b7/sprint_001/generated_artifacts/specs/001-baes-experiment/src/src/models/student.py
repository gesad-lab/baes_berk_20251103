from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Representation of a student in the database."""
    
    __tablename__ = 'students'  # Name of the table in the database
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-generated primary key
    name = Column(String(255), nullable=False)  # Required string field for student name