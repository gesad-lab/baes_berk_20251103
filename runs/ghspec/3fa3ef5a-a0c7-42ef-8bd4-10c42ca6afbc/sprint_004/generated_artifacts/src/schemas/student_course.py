```python
# src/models/student_course.py

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..database.db import Base

class StudentCourse(Base):
    """Model representing the association between students and courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Defining relationships to enable easy access to related objects
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```