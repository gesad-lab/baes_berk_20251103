'''
Pydantic schemas for request and response validation for students, courses, and teachers.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Add this line to include teacher_id
    class Config:
        orm_mode = True
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[CourseResponse]  # Add this line to include courses
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Add this line
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True