'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: EmailStr  # Added email field
class StudentResponse(BaseModel):
    '''
    Schema for returning student data.
    '''
    id: int
    name: str
    email: str  # Added email field
    courses: List['CourseResponse'] = []  # Added relationship to courses
    class Config:
        orm_mode = True
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
    students: List[StudentResponse] = []  # Added relationship to students
    class Config:
        orm_mode = True