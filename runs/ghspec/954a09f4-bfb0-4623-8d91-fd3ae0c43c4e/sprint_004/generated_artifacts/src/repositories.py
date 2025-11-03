```python
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey
from src.database import Base

class StudentCourse(Base):
    """Model for the student_courses table, linking students to their courses"""
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True, nullable=False)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")


# Update the Student model to establish a relationship to courses
class Student(Base):
    """Model for Students, now with a relationship to courses"""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # Existing fields...

    courses = relationship("StudentCourse", back_populates="student")


# Update the Course model to establish a relationship to students
class Course(Base):
    """Model for Courses, now with a relationship to students"""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    # Existing fields...

    students = relationship("StudentCourse", back_populates="course")
```