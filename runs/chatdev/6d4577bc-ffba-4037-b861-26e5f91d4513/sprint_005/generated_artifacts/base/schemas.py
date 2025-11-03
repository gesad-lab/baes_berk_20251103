'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class CourseCreate(BaseModel):  # Added CourseCreate schema
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        from_attributes = True  # Updated to use from_attributes
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Updated to use EmailStr for validation
    courses: List[CourseResponse]  # Added field for courses
    class Config:
        from_attributes = True  # Updated to use from_attributes