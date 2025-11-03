from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class StudentCourse(Base):
    """Model to manage the many-to-many relationship between Students and Courses."""
    
    __tablename__ = 'student_course'

    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)  # Reference to Student
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)      # Reference to Course

    # Define relationships for easier access to related objects
    student = relationship("Student", back_populates="courses")  # Student relationship
    course = relationship("Course", back_populates="students")    # Course relationship

# Note: Make sure to update the Student and Course models to implement back_populates for these relationships.
