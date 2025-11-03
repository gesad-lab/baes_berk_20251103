from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Base declaration for SQLAlchemy models
Base = declarative_base()

class StudentCourse(Base):
    """
    Represents the junction table for the many-to-many relationship 
    between students and courses.

    Attributes:
        student_id (int): The identifier for the student (foreign key).
        course_id (int): The identifier for the course (foreign key).
    """
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"