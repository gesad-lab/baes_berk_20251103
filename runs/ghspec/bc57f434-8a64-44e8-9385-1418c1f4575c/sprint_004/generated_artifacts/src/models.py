```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Importing base class for ORM models

class StudentCourse(Base):
    """Data model representing the enrollment of students in courses, establishing a many-to-many relationship."""

    __tablename__ = 'student_course'

    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)

    # Relationship to access the Student and Course objects
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Note: Ensure that Student and Course models have the inverse relationship defined.
# Example additions to Student and Course models for back_populates could be:
# 
# class Student(Base):
#     ...
#     courses = relationship("StudentCourse", back_populates="student")
# 
# class Course(Base):
#     ...
#     students = relationship("StudentCourse", back_populates="course")
```