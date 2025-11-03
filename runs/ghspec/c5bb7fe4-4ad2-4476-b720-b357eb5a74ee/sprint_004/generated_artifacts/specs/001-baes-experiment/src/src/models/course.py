```python
# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    level = Column(String)

    # Establish relationship with StudentCourses model
    student_courses = relationship('StudentCourses', back_populates='course')

    def __init__(self, name: str, description: str, level: str) -> None:
        """Initialize a Course with name, description, and level."""
        self.name = name
        self.description = description
        self.level = level

    def __repr__(self) -> str:
        """Return a string representation of the Course."""
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"

# Import necessary modules for new association
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base

# Junction table for many-to-many relationship between Student and Course
class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Define relationships to Student and Course models
    student = relationship('Student', backref=backref('courses', cascade='all, delete-orphan'))
    course = relationship('Course', backref='students')

    def __init__(self, student_id: int, course_id: int) -> None:
        """Initialize a StudentCourses association with student_id and course_id."""
        self.student_id = student_id
        self.course_id = course_id
```
