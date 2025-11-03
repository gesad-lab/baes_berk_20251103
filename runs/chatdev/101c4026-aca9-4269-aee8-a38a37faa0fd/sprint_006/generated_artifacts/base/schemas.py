'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    course_ids: List[int] = []  # New field for course IDs
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    course_ids: List[int]  # New field for course IDs
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True