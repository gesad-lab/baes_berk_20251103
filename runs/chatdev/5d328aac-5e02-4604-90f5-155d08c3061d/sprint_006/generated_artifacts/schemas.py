'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Added email field to response
    courses: List[int]  # Add this line to include course IDs
    class Config:
        from_attributes = True  # Updated to use the new configuration key
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: Optional[int]  # Added teacher_id to response
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr