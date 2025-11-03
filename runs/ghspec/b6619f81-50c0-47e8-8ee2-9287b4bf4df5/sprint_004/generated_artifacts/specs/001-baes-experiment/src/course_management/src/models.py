```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming Base is the declarative base for SQLAlchemy

class StudentCourses(Base):
    """
    Represents the many-to-many relationship between students and courses.

    Attributes:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.
    """
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Establish relationships
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update existing Student and Course classes to establish relationships

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # Other existing attributes...
    courses = relationship("StudentCourses", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship("StudentCourses", back_populates="course")
```