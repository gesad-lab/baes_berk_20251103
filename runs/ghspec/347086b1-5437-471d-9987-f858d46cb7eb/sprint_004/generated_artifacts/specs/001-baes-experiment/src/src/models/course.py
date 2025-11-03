```python
# src/models/student.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # Adding a many-to-many relationship with courses through the association table
    courses = relationship("Course", secondary="student_courses", back_populates="students")

class StudentCourse(Base):
    __tablename__ = 'student_courses'  # New association table for many-to-many relationship
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

# Adding back_populates to the Course model for reverse relationship
from .course import Course  # Import Course model for reference

Course.students = relationship("Student", secondary="student_courses", back_populates="courses")
```