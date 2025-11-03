from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourses(Base):
    """
    Represents the junction table that links Students to Courses.

    Attributes:
        student_id (str): Foreign key referencing the Student ID.
        course_id (str): Foreign key referencing the Course ID.
    """
    __tablename__ = 'student_courses'
    
    student_id = Column(ForeignKey('students.id'), primary_key=True, nullable=False)
    course_id = Column(ForeignKey('courses.id'), primary_key=True, nullable=False)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")