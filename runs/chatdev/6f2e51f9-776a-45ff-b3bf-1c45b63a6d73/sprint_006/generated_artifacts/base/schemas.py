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
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr