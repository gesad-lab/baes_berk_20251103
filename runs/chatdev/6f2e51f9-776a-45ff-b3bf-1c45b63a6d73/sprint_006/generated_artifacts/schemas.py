'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Add this line to accept teacher ID
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr