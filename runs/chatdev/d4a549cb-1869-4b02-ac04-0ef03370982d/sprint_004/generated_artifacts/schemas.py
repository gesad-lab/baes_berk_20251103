'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # New email field added
    course_ids: List[int] = []  # List of course IDs for enrollment
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # New email field added
    courses: List[int]  # Include course IDs in the response
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True