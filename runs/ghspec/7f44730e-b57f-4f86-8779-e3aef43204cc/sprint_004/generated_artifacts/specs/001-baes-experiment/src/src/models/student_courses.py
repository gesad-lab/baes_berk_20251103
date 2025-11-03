from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Course(Base):
    """Model representing a Course entity."""
    
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Establishing the many-to-many relationship with Student
    students = relationship("StudentCourse", back_populates="course")

class StudentCourse(Base):
    """Model representing the association table for Student and Course enrollments."""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")