'''
Database models for the application.
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Student(Base):
    '''
    Student entity model.
    '''
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Add this line for email field
    courses = relationship("Course", back_populates="student")  # Establish relationship
class Course(Base):
    '''
    Course entity model.
    '''
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name, required
    level = Column(String, nullable=False)  # Course level, required
    student_id = Column(Integer, ForeignKey('students.id'))  # Foreign key to Student
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Foreign key to Teacher
    student = relationship("Student", back_populates="courses")  # Establish relationship
    teacher = relationship("Teacher", back_populates="courses")  # Establish relationship
class Teacher(Base):
    '''
    Teacher entity model.
    '''
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Establish relationship