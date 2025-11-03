'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
    courses: List[CourseResponse] = []  # Add this line to include courses
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field for Teacher
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field for Teacher