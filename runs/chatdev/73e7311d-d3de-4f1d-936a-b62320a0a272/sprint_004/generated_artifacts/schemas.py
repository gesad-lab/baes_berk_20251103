'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
    course_ids: List[int] = []  # List of course IDs for the relationship
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field to response model
    courses: List[int]  # List of course IDs associated with the student
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