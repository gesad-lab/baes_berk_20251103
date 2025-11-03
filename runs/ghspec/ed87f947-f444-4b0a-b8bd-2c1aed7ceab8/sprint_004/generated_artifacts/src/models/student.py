```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database.base import Base

class StudentCourse(Base):
    """Represents the association between students and courses."""
    __tablename__ = "student_courses"

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

class Student(Base):
    """Model representing a student."""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Relationship to associate many courses with a student
    courses = relationship("StudentCourse", back_populates="student", cascade="all, delete-orphan")

class Course(Base):
    """Model representing a course."""
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Relationship to associate many students with a course
    students = relationship("StudentCourse", back_populates="course", cascade="all, delete-orphan")
```