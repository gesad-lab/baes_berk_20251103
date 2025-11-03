'''
Pydantic models for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class CourseCreate(BaseModel):
    name: str
    level: str