```python
# File: src/models/course.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    
    # Relationship to the junction table
    student_courses = relationship("StudentCourseAssociation", back_populates="course")


class StudentCourseAssociation(Base):
    __tablename__ = 'student_course_associations'
    
    student_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=True)
    
    # Establish relationships with Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="student_courses")
```