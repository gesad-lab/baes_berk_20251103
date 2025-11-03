'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: EmailStr  # Add email field with validation
    courses: List[int] = []  # List of course IDs
class StudentResponse(BaseModel):
    '''
    Schema for returning student data.
    '''
    id: int
    name: str
    email: str  # Add email field
    courses: List[int] = []  # List of course IDs
class CourseCreate(BaseModel):
    '''
    Schema for creating a new course.
    '''
    name: str
    level: str
class CourseResponse(BaseModel):
    '''
    Schema for returning course data.
    '''
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    '''
    Schema for creating a new teacher.
    '''
    name: str
    email: EmailStr  # Add email field with validation
class TeacherResponse(BaseModel):
    '''
    Schema for returning teacher data.
    '''
    id: int
    name: str
    email: str