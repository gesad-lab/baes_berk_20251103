'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    """
    Schema for creating a new student.
    """
    name: str
    email: EmailStr
class StudentResponse(BaseModel):
    """
    Schema for the response of student data.
    """
    id: int
    name: str
    email: str
    courses: List[int]
    class Config:
        from_attributes = True  # Updated from orm_mode to from_attributes
class CourseCreate(BaseModel):
    """
    Schema for creating a new course.
    """
    name: str
    level: str
class CourseResponse(BaseModel):
    """
    Schema for the response of course data.
    """
    id: int
    name: str
    level: str
    class Config:
        from_attributes = True  # Updated from orm_mode to from_attributes
class TeacherCreate(BaseModel):
    """
    Schema for creating a new teacher.
    """
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    """
    Schema for the response of teacher data.
    """
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True  # Updated from orm_mode to from_attributes