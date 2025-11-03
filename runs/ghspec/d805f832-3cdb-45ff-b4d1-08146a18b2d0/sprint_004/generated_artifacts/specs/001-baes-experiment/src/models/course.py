from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class StudentCourse(Base):
    """StudentCourse model representing the association between students and courses.

    This model captures the relationship where a student can enroll in multiple courses.

    Attributes:
        id (int): The unique identifier for the student-course association.
        student_id (int): The ID of the student participating in the course.
        course_id (int): The ID of the course the student is enrolled in.
    """

    __tablename__ = 'student_courses'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update existing models
from models import Student  # Presuming Student model already exists in models.py
from models import Course  # Ensuring Course model is imported

# Add back_populates to Student and Course models to complete relationships
Student.courses = relationship("StudentCourse", back_populates="student")
Course.students = relationship("StudentCourse", back_populates="course")