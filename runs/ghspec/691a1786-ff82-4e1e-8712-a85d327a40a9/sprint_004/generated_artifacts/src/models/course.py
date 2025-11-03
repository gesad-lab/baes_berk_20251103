from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Course(Base):
    """Defines the Course data model for the application."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name
    description = Column(String, nullable=True)  # Optional course description
    
    # Define the relationship to StudentCourse for the many-to-many association
    students = relationship("StudentCourse", back_populates="course")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name})>"