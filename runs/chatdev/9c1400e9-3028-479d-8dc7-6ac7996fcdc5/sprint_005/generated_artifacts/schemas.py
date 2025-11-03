'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field to response
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Email field with validation
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str