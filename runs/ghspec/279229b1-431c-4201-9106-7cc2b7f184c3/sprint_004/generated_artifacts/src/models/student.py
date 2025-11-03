```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Extend existing Student model to include relationship
from .student import Student  # Import Student model to enhance its functionality
from .course import Course  # Import Course model to enhance its functionality

Student.courses = relationship("StudentCourse", back_populates="student")
Course.students = relationship("StudentCourse", back_populates="course")
```