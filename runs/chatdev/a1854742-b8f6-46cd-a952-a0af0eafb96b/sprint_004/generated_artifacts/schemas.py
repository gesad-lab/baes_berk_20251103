'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Add this line for email validation
    course_ids: List[int] = []  # Add this line for course IDs
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Add this line to include email in the response
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