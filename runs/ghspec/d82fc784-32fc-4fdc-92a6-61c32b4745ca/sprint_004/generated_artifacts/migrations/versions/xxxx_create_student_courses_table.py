```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

class Student(Base):
    __tablename__ = 'students'
    # Existing fields...
    courses = relationship("StudentCourse", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    # Existing fields...
    students = relationship("StudentCourse", back_populates="course")
```