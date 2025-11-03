'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Updated to use EmailStr for validation
class CourseCreate(BaseModel):
    name: str  # Required field
    level: str  # Required field
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True