'''
Database models for the application.
'''
from sqlalchemy import Column, Integer, String
from database import Base
class Student(Base):
    '''
    Student model representing the students table in the database.
    '''
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Add email field
class Course(Base):
    '''
    Course model representing the courses table in the database.
    '''
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)