'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Add email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Add email field
    courses: List[int]  # Add courses field to include course IDs
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: List[int]  # Add students field to include student IDs
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True