```python
# File: src/models/student_course.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Establish a relationship to Course through the StudentCourses association table
    courses = relationship("StudentCourses", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    # Establish a relationship to Student through the StudentCourses association table
    students = relationship("StudentCourses", back_populates="course")

class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Define relationships for easier access
    student = relationship(Student, back_populates="courses")
    course = relationship(Course, back_populates="students")
```