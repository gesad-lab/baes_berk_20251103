```python
# src/models/student.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Assuming there's a name column
    email = Column(String, nullable=False, unique=True)  # Assuming there's an email column

    # Establish a many-to-many relationship with courses through the StudentCourseAssociation model
    courses = relationship("StudentCourseAssociation", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)  # Assuming there's a title column
    level = Column(String, nullable=False)  # Assuming there's a level column

    # Establish a many-to-many relationship with students through the StudentCourseAssociation model
    students = relationship("StudentCourseAssociation", back_populates="course")

class StudentCourseAssociation(Base):
    __tablename__ = 'student_course_association'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```