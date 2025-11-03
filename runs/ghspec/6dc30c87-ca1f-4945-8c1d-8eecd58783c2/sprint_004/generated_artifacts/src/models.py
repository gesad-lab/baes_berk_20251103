```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from myapp.database import Base

class StudentCourses(Base):
    """Junction table to link students and courses."""
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationship back to Student and Course
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

class Student(Base):
    """Model representing a student in the database."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # One-to-many relationship with courses
    courses = relationship("StudentCourses", back_populates="student")

class Course(Base):
    """Model representing a course in the database."""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    # One-to-many relationship with students
    students = relationship("StudentCourses", back_populates="course")
```