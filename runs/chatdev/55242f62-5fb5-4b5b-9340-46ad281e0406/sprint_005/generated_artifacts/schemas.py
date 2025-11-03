'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field to response
class CourseCreate(BaseModel):
    name: str  # Course name, required
    level: str  # Course level, required
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str  # Teacher name, required
    email: EmailStr  # Teacher email, required
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
class Config:
    orm_mode = True