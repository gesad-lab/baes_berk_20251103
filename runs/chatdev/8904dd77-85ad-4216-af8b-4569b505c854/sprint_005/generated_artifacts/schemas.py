'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in the response model
class CourseCreate(BaseModel):
    name: str  # Course name
    level: str  # Course level
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str  # Teacher name
    email: str  # Teacher email
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
class Config:
    orm_mode = True