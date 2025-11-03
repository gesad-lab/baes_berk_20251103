```python
# src/database.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class for declarative models
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    # Other fields...

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    # Other fields...

class StudentCourses(Base):
    __tablename__ = 'student_courses'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)  # Foreign key to Student
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)    # Foreign key to Course

    # Relationships for ORM
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Establish relationships in Student and Course models
Student.courses = relationship("StudentCourses", back_populates="student", cascade="all, delete-orphan")
Course.students = relationship("StudentCourses", back_populates="course", cascade="all, delete-orphan")

def initialize_database(db_url: str):
    """
    Initializes the database by creating all tables.

    Parameters:
    db_url (str): The database URL for connection.
    """
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # This handles the creation of all defined tables, including student_courses
```