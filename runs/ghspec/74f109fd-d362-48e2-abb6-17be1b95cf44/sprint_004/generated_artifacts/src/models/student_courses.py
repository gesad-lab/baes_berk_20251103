```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class StudentCourses(Base):
    """Join table for Student and Course many-to-many relationship"""
    
    __tablename__ = 'student_courses'
    
    # Foreign keys for the many-to-many relationship
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    # Relationships for easy access to the relevant student and course
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```