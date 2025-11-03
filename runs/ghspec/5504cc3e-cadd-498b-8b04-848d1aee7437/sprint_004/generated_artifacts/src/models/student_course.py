from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Import the base class from the database module

class StudentCourse(Base):
    """Model representing the association between students and courses."""

    __tablename__ = 'student_course'
    
    # Primary key columns for the junction table
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships to access student and course associated with this association
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students") 

# Update existing Student and Course models to include the relationship in their respective files

# Update in `student.py`
# class Student(Base):
#     ...
#     courses = relationship("StudentCourse", back_populates="student")

# Update in `course.py`
# class Course(Base):
#     ...
#     students = relationship("StudentCourse", back_populates="course")