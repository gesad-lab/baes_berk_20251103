'''
Defines the SQLAlchemy models for the Student, Course, and Teacher entities and Pydantic models for input validation.
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, EmailStr
from typing import List
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", secondary="student_courses")
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    course_ids: List[int] = []  # Add this line to accept course IDs
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Add teacher relationship
    teacher = relationship("Teacher", back_populates="courses")
    students = relationship("Student", secondary="student_courses")
class CourseCreate(BaseModel):
    name: str
    level: str
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Establish relationship with Course
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr