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
    courses: List[int]  # List of course IDs
class CourseCreate(BaseModel):
    name: str  # Course name
    level: str  # Course level
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True