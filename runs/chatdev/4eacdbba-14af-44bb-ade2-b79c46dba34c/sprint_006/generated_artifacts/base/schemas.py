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
    email: str  # Added email field
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):  # New schema for Teacher
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):  # New response schema for Teacher
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True