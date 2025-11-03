'''
Database models for the application.
'''
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Association table for many-to-many relationship
student_course_association = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
class Student(Base):
    '''
    Student model representing the students table in the database.
    '''
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", secondary=student_course_association, back_populates="students")
class Course(Base):
    '''
    Course model representing the courses table in the database.
    '''
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
class Teacher(Base):
    '''
    Teacher model representing the teachers table in the database.
    '''
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)