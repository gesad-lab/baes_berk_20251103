```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    """Represents a Course entity, allowing many-to-many relationships with Students."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    students = relationship("StudentCourses", back_populates="course")

class Student(Base):
    """Represents a Student entity, allowing many-to-many relationships with Courses."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    courses = relationship("StudentCourses", back_populates="student")

class StudentCourses(Base):
    """Join table for Student and Course many-to-many relationship"""

    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```