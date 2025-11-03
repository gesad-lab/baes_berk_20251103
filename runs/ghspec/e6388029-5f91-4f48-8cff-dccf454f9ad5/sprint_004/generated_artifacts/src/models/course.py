```python
# src/models/course.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define relationship to student_courses (association table)
    students = relationship("StudentCourses", back_populates="course")

# Association model for linking Students and Courses
class StudentCourses(Base):
    __tablename__ = "student_courses"

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships to Student and Course entities
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Extend existing Student model to reflect the many-to-many relationship
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Relationship to track courses associated with this student
    courses = relationship("StudentCourses", back_populates="student")
```