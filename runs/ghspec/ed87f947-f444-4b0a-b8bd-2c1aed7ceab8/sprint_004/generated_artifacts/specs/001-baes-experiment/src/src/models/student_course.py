from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    """Model representing the association between students and courses."""
    
    __tablename__ = "student_courses"

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Define relationships for the joins
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")