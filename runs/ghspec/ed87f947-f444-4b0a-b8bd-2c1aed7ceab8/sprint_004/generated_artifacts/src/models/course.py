```python
# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming there's a database module for base classes

class Course(Base):
    """Represents a course entity."""

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # New relationship to StudentCourse to handle many-to-many relationship with Student
    students = relationship("StudentCourse", back_populates="course", cascade="all, delete-orphan")

class StudentCourse(Base):
    """Represents the association between students and courses."""

    __tablename__ = "student_courses"

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships for back-referencing
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```