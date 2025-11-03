# File: src/database/models.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base  # Adjusted to reference the Base from the database module
from .student import Student  # Assuming student model exists in the same directory
from .course import Course    # Assuming course model exists in the same directory

class StudentCourse(Base):
    """
    Represents the association between students and courses they are enrolled in.

    Attributes:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.
        student (Student): The student associated with this enrollment.
        course (Course): The course associated with this enrollment.
    """
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")  # Ensure Student model has a 'courses' attribute
    course = relationship("Course", back_populates="students")    # Ensure Course model has a 'students' attribute

# NOTE: Make sure to add the proper back_populates in the Student and Course models
# to create a bidirectional relationship for retrieving courses for a student 
# and students for a course.