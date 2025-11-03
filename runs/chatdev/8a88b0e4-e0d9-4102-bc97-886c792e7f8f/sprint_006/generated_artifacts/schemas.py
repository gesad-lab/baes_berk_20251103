'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Add email field
    courses: list  # Add courses field to response
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Add teacher_id to associate with a Teacher
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: list  # Add students field to response
    teacher: dict  # Add teacher field to response
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str  # Add email field
    class Config:
        orm_mode = True