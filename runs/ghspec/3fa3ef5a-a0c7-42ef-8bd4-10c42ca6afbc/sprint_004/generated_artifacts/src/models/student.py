from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base


class StudentCourse(Base):
    """Model for the association between students and courses in a many-to-many relationship."""

    __tablename__ = 'student_courses'

    # Composite primary key columns
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Define relationships to Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")