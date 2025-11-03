```python
# course_management/src/db/database.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other student fields...


class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # Other course fields...


class StudentCourse(Base):
    """Model for representing the relationship between students and courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")


# Establishing bi-directional relationships
Student.courses = relationship("StudentCourse", back_populates="student")
Course.students = relationship("StudentCourse", back_populates="course")


def init_db():
    """Initialize the database."""
    engine = create_engine('sqlite:///your_database.db')  # Specify your database URL
    Base.metadata.create_all(engine)


# Additional helper functions for database operations can be added here
# Ensure error handling and integrity checks as needed.
```