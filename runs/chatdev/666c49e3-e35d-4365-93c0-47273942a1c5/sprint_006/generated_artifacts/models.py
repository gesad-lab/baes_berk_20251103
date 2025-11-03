'''
Defines the SQLAlchemy model for the Student, Course, and Teacher entities and the Pydantic models for request validation.
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
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Add foreign key reference
    students = relationship("Student", secondary="student_courses", back_populates="courses")
    teacher = relationship("Teacher", back_populates="courses")  # Establish relationship with Teacher
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int = None  # Make teacher_id optional
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Establish relationship with Course
class TeacherCreate(BaseModel):
    name: str
    email: str