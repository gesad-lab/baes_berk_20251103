'''
Defines the SQLAlchemy models for the application, including Student, Course, and Teacher entities.
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base  # Import Base from the new base.py
class Student(Base):
    '''
    Model for the Student entity.
    '''
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", secondary="student_courses")
class Course(Base):
    '''
    Model for the Course entity.
    '''
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Add this line
    students = relationship("Student", secondary="student_courses")
    teacher = relationship("Teacher")  # Add this line to establish the relationship
class StudentCourses(Base):
    '''
    Model for the association table between Student and Course entities.
    '''
    __tablename__ = 'student_courses'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
class Teacher(Base):
    '''
    Model for the Teacher entity.
    '''
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)