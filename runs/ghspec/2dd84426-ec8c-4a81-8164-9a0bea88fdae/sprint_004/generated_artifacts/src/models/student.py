from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Base class for declarative model definitions
Base = declarative_base()

class StudentCourses(Base):
    """
    Model class representing the association between students and courses.
    This establishes a many-to-many relationship between the Student and Course entities.
    """
    __tablename__ = 'student_courses'
    
    # Foreign Key to the student table
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    # Foreign Key to the course table
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationship to access the associated Student object
    student = relationship("Student", back_populates="courses")
    # Relationship to access the associated Course object
    course = relationship("Course", back_populates="students")