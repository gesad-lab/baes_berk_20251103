```python
# src/models.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # Other existing fields...

    # Relationship to associate students with courses
    courses = relationship("StudentCourses", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # Other existing fields...

    # Relationship to associate courses with students
    students = relationship("StudentCourses", back_populates="course")

class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```