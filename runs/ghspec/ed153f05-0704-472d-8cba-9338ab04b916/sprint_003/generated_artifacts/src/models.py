# Updated .env for Course Feature Configurations

COURSE_NAME_MIN_LENGTH=3
COURSE_NAME_MAX_LENGTH=100
COURSE_LEVELS=beginner,intermediate,advanced

# src/models.py
import os
from sqlalchemy import Column, Integer, String
from src.database import Base

class Course(Base):
    """Course model for managing course data."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(os.getenv('COURSE_NAME_MAX_LENGTH')), nullable=False)
    level = Column(String, nullable=False)

    def __init__(self, name: str, level: str):
        """Initialize a Course instance."""
        self.name = name
        self.level = level

    def __repr__(self):
        """Represent the Course object as a string."""
        return f"<Course(name={self.name}, level={self.level})>"