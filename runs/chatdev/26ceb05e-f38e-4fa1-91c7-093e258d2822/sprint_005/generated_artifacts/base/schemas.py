'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in the response model
    courses: List[int] = []  # List of course IDs the student is enrolled in
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