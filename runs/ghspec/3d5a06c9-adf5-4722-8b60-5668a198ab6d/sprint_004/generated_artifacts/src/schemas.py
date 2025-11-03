```python
# File: src/models.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Enrollment(Base):
    """
    Enrollment model to represent a many-to-many relationship
    between Students and Courses. Each Enrollment instance
    associates a Student with a Course.
    """
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, index=True)  # Auto-incrementing primary key
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)  # Foreign key referencing Student
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)    # Foreign key referencing Course

    # Establish relationships for easy access
    student = relationship("Student", back_populates="enrollments")  # Back reference to Student model
    course = relationship("Course", back_populates="enrollments")    # Back reference to Course model

# Ensure that the Student and Course models have a relationship defined back to this model
# For Students:
# class Student(Base):
#      ...
#      enrollments = relationship('Enrollment', back_populates='student')

# For Courses:
# class Course(Base):
#      ...
#      enrollments = relationship('Enrollment', back_populates='course')
```