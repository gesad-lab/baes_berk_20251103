'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # New email field added with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # New email field added to response
    courses: list  # Added to include courses in the response
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: list  # Added to include students in the response
    class Config:
        orm_mode = True