from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Assuming there's a base class defined in base.py

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # Other fields as previously defined
    student_courses = relationship("StudentCourse", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    student_courses = relationship("StudentCourse", back_populates="course")

class StudentCourse(Base):
    """Represents the association between students and courses."""

    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="student_courses")
    course = relationship("Course", back_populates="student_courses") 

