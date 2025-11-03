```python
from extensions import db  # Assuming you use SQLAlchemy for database interaction
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Student(db.Model):
    """Student model to represent a student entity in the system."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for the student
    name = Column(String(100), nullable=False)  # Name of the student
    email = Column(String(100), unique=True, nullable=False)  # Email of the student
    # Establishing many-to-many relationship with Course through StudentCourses
    courses = relationship('Course', secondary='student_courses', back_populates='students')

class Course(db.Model):
    """Course model to represent a course entity in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)  # Unique identifier for the course
    name = Column(String(100), nullable=False)  # Name of the course
    level = Column(String(50), nullable=False)  # Level of the course (e.g., beginner, intermediate)
    # Establishing many-to-many relationship with Student through StudentCourses
    students = relationship('Student', secondary='student_courses', back_populates='courses')

class StudentCourses(db.Model):
    """Junction table for the many-to-many relationship between students and courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)  # Student identifier
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)  # Course identifier
```