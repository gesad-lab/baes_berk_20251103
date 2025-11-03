```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    """Model to represent the association between students and courses."""
    
    __tablename__ = 'student_courses'
    
    # Establish composite primary key for student and course relationships
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships to enable accessing related Student and Course objects
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Extend existing Student and Course models to include relationship
from .student import Student  # Ensure to import Student model
from .course import Course    # Ensure to import Course model

# Define back_populates attributes in existing Student and Course models
Student.courses = relationship("StudentCourse", back_populates="student")
Course.students = relationship("StudentCourse", back_populates="course")
```