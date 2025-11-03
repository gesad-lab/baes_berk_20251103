from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    # Establish a relationship with the courses through the StudentCourse association table
    courses = relationship("StudentCourse", back_populates="student", cascade="all, delete-orphan")
    
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")