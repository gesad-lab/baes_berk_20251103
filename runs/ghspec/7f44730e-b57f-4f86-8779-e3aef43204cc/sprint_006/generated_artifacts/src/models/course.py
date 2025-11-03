# src/models/course.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=True)  # New foreign key to Teacher

    teacher = relationship("Teacher", back_populates="courses")  # Define relationship for ORM access

    def __repr__(self):
        """Return a string representation of the Course object."""
        return f"<Course(id='{self.id}', name='{self.name}', teacher_id='{self.teacher_id}')>"