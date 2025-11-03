'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    course_ids: List[int] = []  # List of course IDs
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[int] = []  # List of course IDs
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int = None  # Add this line to accept teacher ID
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int = None  # Add this line to return teacher ID
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True