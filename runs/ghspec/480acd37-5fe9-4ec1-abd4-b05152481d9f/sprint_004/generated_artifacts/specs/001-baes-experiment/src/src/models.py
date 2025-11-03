```python
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    """Model representing the association between Students and Courses."""
    
    __tablename__ = 'student_courses'

    # Composite primary key consisting of student_id and course_id
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Establishing relationships to the Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Ensure that you are importing the Student and Course models properly in your application
# This code assumes that Student and Course models are defined and that 'students' and 'courses' tables exist.
```