'''
Defines the SQLAlchemy models for the Student, Course, and Teacher entities.
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base  # Import Base from the new base module
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", secondary="student_courses", back_populates="students")
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Added foreign key for teacher
    teacher = relationship("Teacher", back_populates="courses")  # Relationship to Teacher
    students = relationship("Student", secondary="student_courses", back_populates="courses")
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Relationship to Course