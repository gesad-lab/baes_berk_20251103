# src/models/course.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.database import Base

class Course(Base):
    """Course model representing educational courses offered in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    
    # Relationship field to link the Course model to the StudentCourse join table
    students = relationship("StudentCourse", back_populates="course")
    
    def __repr__(self):
        """Return a string representation of the Course model."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"