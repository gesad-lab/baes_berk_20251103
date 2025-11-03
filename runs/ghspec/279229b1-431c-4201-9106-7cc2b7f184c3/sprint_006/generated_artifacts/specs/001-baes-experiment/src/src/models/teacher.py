# File: src/models/course.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming there's a base model or similar
from .teacher import Teacher  # Import the Teacher model

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Add the new teacher_id field as a foreign key referencing the Teacher model
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Establish a relationship with the Teacher model
    teacher = relationship('Teacher', back_populates='courses')

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>" 

# Assuming the Teacher model is defined like this with relationship back to courses
# You would need to add this in src/models/teacher.py
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # This establishes a one-to-many relationship - One Teacher can have many Courses
    courses = relationship('Course', back_populates='teacher')