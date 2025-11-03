'''
Database models for the application.
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Student(Base):
    '''
    Student entity model.
    '''
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Added email field
    courses = relationship("Course", secondary="student_courses", back_populates="students")
class Course(Base):
    '''
    Course entity model.
    '''
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship("Student", secondary="student_courses", back_populates="courses")
class Teacher(Base):
    '''
    Teacher entity model.
    '''
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)