'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Existing email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Existing email field to response
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added teacher_id to allow assignment of a teacher
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Required field for Teacher
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr  # Required field for Teacher
    class Config:
        orm_mode = True