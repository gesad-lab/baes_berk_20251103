```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class StudentCourse(db.Model):
    """Model representing the association between students and courses."""
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)
    
    # Define relationships to Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")


# Make sure to reference the associations in the Student and Course models.
from app.models.student import Student  # Ensure this import is consistent with your project structure
from app.models.course import Course  # Ensure this import is consistent with your project structure

# Extend the Student model to include a relationship to StudentCourse
Student.courses = relationship("StudentCourse", back_populates="student", cascade="all, delete, delete-orphan")

# Extend the Course model to include a relationship to StudentCourse
Course.students = relationship("StudentCourse", back_populates="course", cascade="all, delete, delete-orphan")
```