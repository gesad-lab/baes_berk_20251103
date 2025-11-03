'''
Defines the SQLAlchemy model for the Student and Course entities and the Pydantic models for request validation.
'''
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Add email field
    courses = relationship("Course", secondary="student_courses", back_populates="students")
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship("Student", secondary="student_courses", back_populates="courses")
class CourseCreate(BaseModel):
    name: str
    level: str