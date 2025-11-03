from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # Relationship to link students with courses
    courses = relationship("StudentCourse", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String)

    # Relationship to link courses with students
    students = relationship("StudentCourse", back_populates="course")

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    # Establishing relationships with Student and Course models
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")