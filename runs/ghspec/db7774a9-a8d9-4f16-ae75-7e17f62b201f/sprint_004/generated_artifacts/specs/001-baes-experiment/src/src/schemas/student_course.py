```python
# src/models/student_course.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class StudentCourse(Base):
    """Junction table for the many-to-many relationship between students and courses."""
    
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationship for accessing associated student and course objects
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```