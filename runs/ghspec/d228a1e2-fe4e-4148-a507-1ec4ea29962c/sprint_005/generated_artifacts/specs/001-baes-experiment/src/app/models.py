from sqlalchemy import Column, Integer, String
from app import db

class Teacher(db.Model):
    """Model representing a teacher in the system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for each teacher
    name = Column(String, nullable=False)     # Teacher's name (required)
    email = Column(String, nullable=False, unique=True)  # Teacher's email (required and must be unique)