'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Added email field to response
    courses: List['CourseResponse'] = []  # Added courses field to response
class CourseCreate(BaseModel):
    name: str  # Required field
    level: str  # Required field
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: List[StudentResponse] = []  # Added students field to response
    class Config:
        orm_mode = True