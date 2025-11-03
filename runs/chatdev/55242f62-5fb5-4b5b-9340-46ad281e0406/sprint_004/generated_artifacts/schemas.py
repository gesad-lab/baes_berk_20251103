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
    courses: List[int]  # List of course IDs the student is enrolled in
class CourseCreate(BaseModel):
    name: str  # Course name, required
    level: str  # Course level, required
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True