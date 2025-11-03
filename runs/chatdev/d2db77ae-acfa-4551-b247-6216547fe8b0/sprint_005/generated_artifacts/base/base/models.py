'''
Defines the SQLAlchemy models for the Student and Course entities and Pydantic models for input validation.
'''
from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel, EmailStr
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
class CourseCreate(BaseModel):
    name: str
    level: str