'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # New email field added
    courses: List[str]  # New field for courses
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # New email field added
    courses: List[str]  # New field for courses
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True